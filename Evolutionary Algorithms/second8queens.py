# knapsack.py
# What should we take in our knapsack for a weekend road trip?
#
# In this problem, you will use a genetic algorithm to optimize your packing
# list for an upcoming road trip. You are provided a data file containing a
# list of potential items along with their associated value and weight. Your
# goal is to determine what you should bring that maximizes the total value of
# items while maintaining a weight under 5 kg.

import numpy as np
import matplotlib.pyplot as plt
import numpy.random as r
from numpy.core.multiarray import ndarray


def initialize(m, N):
    '''Initialize a population of m individuals with genotypes of length N.'''

    # Variables for randint [r_min, r_max), [0,2) is binary

    return r.randint(r_min, r_max, (m, N))


def fitness(population):
    '''Compute the fitness of every individual in the population according to
    the provided value of available items, weight of available items, and
    maximum allowable weight.'''
    fitnesses = []

    for individual in population:
        tot = 0

        for i in range(N):
            for j in range(N):
                diff = j - i
                if individual[i] == individual[j] - diff:
                    tot += 1
                if individual[i] == individual[j]:
                    tot += 1
                if individual[i] == individual[j] + diff:
                    tot += 1

        fitnesses.append(tot)
    return np.array(fitnesses)


def selectparents(population, n, k):
    '''Tournament selection (size k) of n parents from a given population stored in a (n, N) sized array'''
    x = r.randint(population.shape[0], size=(n,k))
    indicies = x.min(axis=1)
    return population[indicies,]


def crossover(parents, pc, n, N):
    '''Perform one-point crossover on pairs of parents with probability pc stored in a (n,N) sized array.'''

############
    ######################### BROKEN BROKEN BROKEN BROKEN BROKEN
############


    children = np.empty((n, N), dtype='int')

    for i in range(int(n / 2)):
        i1 = 2 * i
        i2 = 2 * i + 1

        for x_point in range(N):
            if r.rand() < pc:
                children[i1, :] = np.hstack((parents[i1, :x_point], parents[i2, x_point:]))
                children[i2, :] = np.hstack((parents[i2, :x_point], parents[i1, x_point:]))

    return children


def mutation(children, pm):
    '''Perform bit-flip mutation on children with per-gene probability pm.'''

    for x in np.nditer(children, op_flags=['readwrite']):
        if r.rand() < pm:
            x[...] = r.randint(r_min, r_max)

    return children


def sort(population, population_fitness):
    '''Sorting a population by a provided fitness.'''

    # Sort pop and fitness array
    ind_sort = population_fitness.argsort() # make an array of indexes that would sort the array
    pop_fit = population_fitness[ind_sort] # sort the fitness array
    pop = population[ind_sort] # sort the 2d array based on the sorted indices of the finess array
    # higher indexes = higher fitness

    return pop, pop_fit


def survivorselection(parents, children):
    pop = np.vstack((parents,children))
    pop_fit = fitness(pop)
    pop, pop_fit = sort(pop, pop_fit)
    return pop[:m]


np.set_printoptions(threshold=np.nan)

# Set relevant parameters ##############################################################################################
r_min = 0  # genotype min
r_max = 8  # and max

m = 500  # number of individuals
N = 8  # genotype length

n = 500  # num parents to select/breed (and children produced, b/c p:c == 1:1 for 1pt crossover)
k = 5  # tournament size

pc = 0.50  # probability of crossover
pm = 0.01  # probability of mutation

r.seed()  # Set seed for repeatability
# ######################################################################################################################

# Run genetic algorithm

# Initialize
p = initialize(m, N)

# 1st data-point for graph
p_fit = fitness(p)
best_fit = [p_fit[-1]]
avg_fit = [np.average(p_fit)]

# Run the algorithm
generation = 0
while generation < 100 and p_fit[0] != 0:

    print("\n\n\n\nGENGENGEN")


    print("base", p)

    generation += 1

    # Determine fitness:
    p_fit = fitness(p)


    # Sort population by fitness:
    p, p_fit = sort(p, p_fit)

    print("sort", p)

    print(p)

    # Breed:
    # Parent Selection
    P = selectparents(p, n, k) # requires a sorted array to work properly

    print("parents", P)

    # Crossover
    C = crossover(P, pc, n, N)

    print("x", C)

    # Mutation
    M = mutation(C, pm)

    print("m", M)

    # Select Survivors:
    p = survivorselection(P, M)

    print("select", p)

    # Record the best and average fitness over time
    best_fit.append(p_fit[0])
    avg_fit.append(np.average(p_fit))

# Plot the best and average fitness over time



plt.plot(best_fit, 'r-')
plt.plot(avg_fit, 'b-')
plt.show()