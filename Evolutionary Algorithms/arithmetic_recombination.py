# Quin H. Arithmetic Recombination
import numpy as np
import numpy.random as r

def r_ind():
    return r.randint(5)

def simple_a_r(target_1, target_2, a):
    a1 = np.copy(target_1)
    a2 = np.copy(target_2)

    # Random number
    c = r_ind()

    # Do an average for everything after c
    b1 = np.concatenate((a1[:c], (a*a1[c:]) + ((1-a)*a2[c:])))
    b2 = np.concatenate((a2[:c], (a*a2[c:]) + ((1-a)*a1[c:])))

    return b1, b2


def single_a_r(target_1, target_2, a):
    a1 = np.copy(target_1)
    a2 = np.copy(target_2)

    # Random number
    c = r_ind()

    # Copy a1 and a2
    b1 = np.copy(a1)
    b2 = np.copy(a2)

    # Change just the selected (b's) index based off the parent's (a's) average
    b1[c] = (a * a1[c]) + ((1 - a) * a2[c])
    b2[c] = (a * a2[c]) + ((1 - a) * a1[c])

    #could have been solved with a temp variable but meh

    return b1, b2


def whole_a_r(target_1, target_2, a):
    a1 = np.copy(target_1)
    a2 = np.copy(target_2)

    # Average all the things
    b1 = (a * a1) + ((1 - a) * a2)
    b2 = (a * a2) + ((1 - a) * a1)

    return b1, b2


r.seed(4)

p1 = [8.5,6.1,5.9,1.4,2.2]
p2 = [6.8,9.0,6.3,0.1,5.7]

a = 0.5

sm1, sm2 = simple_a_r(p1, p2, a)
si1, si2 = single_a_r(p1, p2, a)
wh1, wh2 = whole_a_r(p1, p2, a)

print("Original:", p1, p2, sep='\t')
print("Simple:\t", sm1, sm2, sep='\t')
print("Single:\t", si1, si2, sep='\t')
print("Whole:\t", wh1, wh2, sep='\t')
