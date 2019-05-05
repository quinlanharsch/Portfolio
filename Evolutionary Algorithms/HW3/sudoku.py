#! /usr/bin/env python
"""Solve a Sudoku puzzle using a genetic algorithm."""
# ### Imports ##########################################################################################################
import argparse
import os
import numpy as np
import numpy.random as r
import matplotlib.pyplot as plt

# ### Globals ##########################################################################################################
parser = argparse.ArgumentParser(description="Solve a Sudoku puzzle using a genetic algorithm.")
parser.add_argument('-d', '--datafile', help="path to text file containing partially-filled Sudoku puzzle(s)",
                    default=os.path.join(os.getcwd(), 'puzzles.txt'))
parser.add_argument('-i', '--index', help="index of puzzle in data file", type=int, default=1)
parser.add_argument('-s', '--seed', help="seed for random number generator", type=int, default=0)

# ### Design Parameters ################################################################################################
gen_limit = 200  # max number of generations the algorithm can run
mu = 250 # (half) the number of individuals in population
mu *= 2

n = mu  # Number of Parents (default is mu)
c = 0.3  # "Spinner wedge similarity" (higher values give a flatter distribution for parent selection)
# This variable is subtracted by the existing probabilities; making low values more likely and lower values less likely.

pc = 0.9  # Probability of crossover by row
pm = 1.0/9  # Probability of crossover happening in a row

elitism = 3  # Number of parents conserved


# ### Main ############################################################################################################
def main(args):
    # Parse input arguments
    datafile = os.path.expanduser(args.datafile)
    index = args.index
    seed = args.seed

    # Set random number generator
    r.seed(seed)

    # Read requested Sudoku puzzle from file
    print("Reading Sudoku puzzle from file:", datafile)
    puzzles = np.genfromtxt(datafile, delimiter=1, dtype=int)

    # ### Run genetic algorithm
    print("Running genetic algorithm...")

    puzzle = puzzles[index]
    print("Loaded Puzzle:", puzzle.reshape((9,9)), sep='\n')

    population = initialize(mu, puzzle)
    best_fits = [np.infty]
    avg_fits = [np.infty]
    # updated in fitness():

    generation = 1
    while generation < gen_limit + 1 and best_fits[-1] != 0:

        fits = fitness(population)
        best_fits.append(np.min(fits))
        avg_fits.append(np.average(fits))

        parents = selectparents(population, fits, n)
        children = crossover(parents, pc)
        children = mutation(children, puzzle, pm)
        population = selectsurvivors(children, parents)

        print("Gen:", generation, " \tBest fitness:", best_fits[-1])
        if fits[-1] == 0 or generation == gen_limit:
            print(population[np.argmin(fits)].reshape((9,9)))

        generation += 1

# ### Plot results (credit to Eicholtz) ################################################################################
    plt.plot(np.arange(1, len(best_fits)), best_fits[1:], label='Best')
    plt.plot(np.arange(1, len(avg_fits)), avg_fits[1:], label='Average')
    plt.legend()
    plt.xlabel('Generations')
    plt.ylabel('Fitness')
    plt.show()


# ### Functions ########################################################################################################
def initialize(mu, puzzle): #VV
    '''Initialize a population of mu individuals representing potential Sudoku solutions.'''

    population = np.empty((mu, 81), dtype=int)

    for m in range(mu):
        individual = np.copy(puzzle.reshape((9,9)))
        for row in individual:
            available = np.delete(np.arange(1, 10), np.unique(row)[1:] - 1)  # makes a list of numbers not in row
            for i in range(9):
                if row[i] == 0:
                    selected = r.choice(available)                                          # pick a number from list
                    row[i] = selected                                                       # add it to the individual
                    available = np.delete(available, np.argwhere(available == selected))    # remove it from the list
        population[m] = individual.ravel()

    return population


def fitness(population): #VV
    '''Compute the fitness of every individual in the population.'''

    fits = []

    for i in range(len(population)):
        target = population[i].reshape((9,9))
        # Boxes
        t = 162
        for r in range(3):
            for c in range(3):
                t -= np.unique(target[3 * r:(3 * r) + 3, 3 * c:(3 * c) + 3]).size
        # Columns
        for col in target.T:
            t -= np.unique(col).size

        fits.append(t)

    return np.array(fits, dtype=int)


def selectparents(population, fitnesses, n): #VV
    '''Select n parents from the current population. Using Roulette wheel selection'''
    m_fit = (np.max(fitnesses) + c) - fitnesses  # "flips" the graph so higher numbers have lower m_fitness
    p = m_fit / np.sum(m_fit)  # normalizes for 0..1 for the spinner wedges
    ind = r.choice(mu, n, p=p)  # spins the spinner n times to get corresponding indeces
    return population[ind]


def crossover(parents, pc):
    '''Perform uniform crossover on Sudoku rows from pairs of parents with probability pc.'''

    children = np.empty((n, 81), dtype=int)

    for i in range(int(n/2)):
        p1 = parents[i].reshape((9,9))
        p2 = parents[i+1].reshape((9,9))
        c1 = np.copy(p1)
        c2 = np.copy(p2)
        for row in range(9):
            if r.rand() < pc:
                c1[row] = p2[row]
                c2[row] = p1[row]
        children[i] = c1.ravel()
        children[i+1] = c2.ravel()

    return children


def mutation(children, puzzle, pm):
    '''Perform swap mutation on Sudoku rows of children with per-row probability pm.'''

    # make a "mask" where locked numbers are one and
    mask = np.ones((9,9), dtype=int)
    mask[np.nonzero(puzzle.reshape((9,9)))] = 0

    for child in children:
        for row in range(9):
            if r.rand() < pm:
                sw = 9*row + r.choice(9, 2, replace=False, p=mask[row]/np.sum(mask[row]))  # choose where to swap
                child[sw[0]], child[sw[1]] = child[sw[1]], child[sw[0]]  # swap

    return children


def selectsurvivors(children, parents):
    '''Generational selection of survivors from mutated children.'''
    return sort(np.vstack((parents, children)))[:mu]
    # return np.vstack((sort(parents)[:elitism], sort(np.vstack(children))[elitism:mu]))


def sort(a): return a[np.argsort(fitness(a))]


# ### Body #############################################################################################################
if __name__ == '__main__':
    main(parser.parse_args())