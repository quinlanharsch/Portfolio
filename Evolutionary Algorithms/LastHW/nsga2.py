# nsga2.py
# Functions related to the nondominated sorting genetic algorithm
# described in the following paper:
#
# K. Deb, A. Pratap, S. Agarwal, and T. Meyarivan, "A Fast and Elitist
# Multiobjective Genetic Algorithm: NSGA-II", in IEEE Transactions on
# Evolutionary Computation, vol. 6, no. 2, 2002, pp. 182-197.

import os
import numpy as np
import matplotlib.pyplot as plt
from numpy.core.multiarray import ndarray


def main():
    # Set relevant parameters
    root = os.getcwd()  # root directory that contains the data file
    filename = "fitness.txt"
    savefile = "distance.txt"

    # Load data from file
    f = np.loadtxt(os.path.join(root, filename))

    # Compute Pareto fronts using fast nondominated sorting
    p = ndsort(f)

    # Compute crowding distance (each front is handled separately)
    d = crowddist(f, p)

    # Save the crowding distance results to file
    np.savetxt(os.path.join(root, savefile), d, fmt='%0.2f')


def ndsort(f):
    p = np.zeros(f.shape[0])

    # Part 1: generate Sp and np

    n = []  # domination count (dominate p) [int]
    S = []  # set of solutions that p dominates [[solutions]]

    for i in range(f.shape[0]):
        n.append(0)
        S.append([])
        for j in range(f.shape[0]):
            if i == j: continue # if i and j are the same solution continue
            elif a_dominates_b(f[i],f[j]):  # if i dominates j
                S[i].append(j)
            elif a_dominates_b(f[j],f[i]):  # if i is dominated by j
                n[i] += 1

    # Part 2: use Sp and np to find Pareto-fronts

    n = np.array(n)
    S = np.array(S)

    Q = np.array(np.where(n == 0))[0]  # find where np==0
    front = 1
    while True:
        next_Q = []
        for k in Q:
            if S[k] == 0:
                continue
            for l in S[k]:
                n[l] -= 1
                if n[l] == 0:
                    next_Q.append(l)

        p[Q] = front

        if not next_Q: break
        Q = next_Q

        front += 1

    # Pyplot, must be 2d
    f1 = f[:,0].ravel()
    f2 = f[:,1].ravel()
    plt.plot(f1[np.where(p == 1)], f2[np.where(p == 1)], 'bo')
    plt.plot(f1[np.where(p == 2)], f2[np.where(p == 2)], 'o', color='#ffa500')
    plt.plot(f1[np.where(p == 3)], f2[np.where(p == 3)], 'go')
    plt.plot(f1[np.where(p == 4)], f2[np.where(p == 4)], 'ro')
    plt.plot(f1[np.where(p == 5)], f2[np.where(p == 5)], 'mo')
    plt.plot(f1[np.where(p == 6)], f2[np.where(p == 6)], 'ko')
    plt.show()

    # Return an array of Parent front indices for each data point
    return p


def a_dominates_b(a,b):  # a&b shape=(2,)
    return (a[0] <= b[0] and a[1] <= b[1]) and (a[0] < b[0] or a[1] < b[1])


def crowddist(f, p):
    d = np.array(range(f.shape[0]), dtype=float)

    front_1 = np.array(np.where(p == 1))[0]  # find where p==1
    front_f = f[front_1]

    d[[0,-1]] = np.inf
    for i in range(f.shape[1]):  # for as many fn's we have
        fn: ndarray = -np.sort(-front_f[:, i].ravel())  # sort the fn() vals
        norm = fn[0] - fn[-1]  # max - min
        for j in range(1, fn.shape[0]-1):  # take the distance of each
            d[j] += (fn[j-1] - fn[j+1])/norm

    # Return the crowding distance metric for each data point
    print("d:", d)
    return d


if __name__ == "__main__":
    main()
