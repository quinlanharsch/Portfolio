import argparse
import os
import numpy as np
import numpy.random as r
import matplotlib.pyplot as plt

def fitness(population):
    '''Compute the fitness of every individual in the population.'''

    fits = np.empty(1, dtype=int)

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

        fits[i] = t

    return fits


'''================================================================================================================='''

r.seed(4)

puzzles = np.genfromtxt("puzzles.txt", delimiter=1, dtype=int)
puzzle = puzzles[1]
print(puzzle.reshape((9,9)))

population = np.empty((1, 81), dtype=int)

for m in range(1):

    individual = np.copy(puzzle.reshape((9,9)))
    for row in individual:

        available = np.delete(np.arange(1, 10), np.unique(row)[1:] - 1)  # makes a list of numbers not in row

        for i in range(9):
            if row[i] == 0:

                selected = r.choice(available)                                          # pick a number from list
                row[i] = selected                                                       # add it to the individual
                available = np.delete(available, np.argwhere(available == selected))    # remove it from the list

    population[m] = individual.ravel()

print(population[0].reshape((9,9)))

print(fitness(population))