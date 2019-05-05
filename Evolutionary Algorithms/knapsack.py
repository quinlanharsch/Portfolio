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
    r_min = 0
    r_max = 2

    return r.randint(r_min, r_max, (m, N))


def fitness(population, value, weight, maxweight):
    '''Compute the fitness of every individual in the population according to
    the provided value of available items, weight of available items, and
    maximum allowable weight.'''

    pop_fit = []

    for i in range(m):
        g = population[i]
        if g*weight > 5:
            g_value = np.sum(g * value)
        else:
            g_value = np.sum((g * value) - (g * weight - 5))
        pop_fit.append(g_value)

    return np.array(pop_fit)


def selectparents(population, n, k, N):
    '''Tournament selection (size k) of n parents from a given population stored in a (n, N) sized array'''

    parents = np.empty((n, N), dtype='int')

    for i in range(n):
        r_nums = r.randint(0, n, k)
        parents[i, :] = population[np.max(r_nums),:]

    return np.array(parents)


def crossover(parents, pc, n, N):
    '''Perform one-point crossover on pairs of parents with probability pc stored in a (n,N) sized array.'''

    children = np.empty((n, N), dtype='int')

    for i in range(int(n / 2)):
        i1 = 2 * i
        i2 = 2 * i + 1

        if r.rand() < pc:
            x_point = r.randint(0, N-1)
            children[i1, :] = np.hstack((parents[i1, :x_point], parents[i2, x_point:]))
            children[i2, :] = np.hstack((parents[i2, :x_point], parents[i1, x_point:]))

        else:
            children[i1, :] = parents[i1, :]
            children[i2, :] = parents[i2, :]

    return children


def mutation(children, pm):
    '''Perform bit-flip mutation on children with per-gene probability pm.'''

    for x in np.nditer(children, op_flags=['readwrite']):
        if r.rand() < pm:
            x[...] = np.abs(x - 1)

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
    return children

# Set relevant parameters ##############################################################################################

generations = 50

m = 10  # number of individuals
N = 12  # genotype length

n = 10  # num parents to select/breed (and children produced, b/c p:c == 1:1 for 1pt crossover)
k = 2  # tournament size

pc = 0.50  # probability of crossover
pm = 0.01  # probability of mutation

maxweight = 5

# Set seed for repeatability
r.seed(4)

# ######################################################################################################################

# Read list of items from file
# [name, value, weight]
l_items = np.genfromtxt('listofitems.csv', delimiter=',')
value = l_items[:, 1].ravel()
weight = l_items[:, 2].ravel()
# (max weight above...)

# Run genetic algorithm

# Initialize
p = initialize(m, N)

# 1st data-point for graph
p_fit = fitness(p, value, weight, maxweight)
best_fit = [p_fit[-1]]
avg_fit = [np.average(p_fit)]

# Run the algorithm
for generation in range(generations):
    # Determine fitness:
    p_fit = fitness(p, value, weight, maxweight)

    # Sort population by fitness:
    p, p_fit = sort(p, p_fit)

    # Breed:
    # Parent Selection
    P = selectparents(p, n, k, N) # requires a sorted array to work properly
    # Crossover
    C = crossover(P, pc, n, N)
    # Mutation
    M = mutation(C, pm)

    # Select Survivors:
    p = survivorselection(P, M)

    # Record the best and average fitness over time
    best_fit.append(p_fit[-1])
    avg_fit.append(np.average(p_fit))

# Plot the best and average fitness over time

print("Best: ", p.max(axis=0))
print("Fitness- ", p_fit.max())
print("Weight- ", np.sum(p.max(axis=0)*weight))

plt.plot(best_fit, 'r-')
plt.plot(avg_fit, 'b-')
plt.show()