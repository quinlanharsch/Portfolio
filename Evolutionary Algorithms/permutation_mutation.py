# Quin H. Inversion and Swap Permutation Mutations
import numpy as np
import numpy.random as r

def r_ind(n):
    return r.choice(child.size, n, replace=False)


def swap_m(target):
    a = np.copy(target)

    # Random 2 numbers
    c = r_ind(2)
    print("(Swap on ", c, ')', sep='')  # error checking

    # Tuple unpacking swap operation
    a[[c[0], c[1]]] = a[[c[1], c[0]]]
    return a


def inversion_m(target):
    a = np.copy(target)

    # Random 2 numbers
    c = np.sort(r_ind(2))
    print("(Invert on ", c, ')', sep='')  # error checking

    # Inversion
    a[c[0]:c[1]] = a[c[0]:c[1]][::-1]
    return a


#Set seed
r.seed(4)

child = np.array([1, 2, 3, 4, 5, 6, 7])

print("Original: ", child, "\n")
print("Swap mutation: ", swap_m(child), "\n")
print("Inversion mutation: ", inversion_m(child), "\n")
