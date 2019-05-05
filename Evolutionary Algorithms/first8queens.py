import numpy as np
import numpy.random as r

# ######################################################################################################################
print("64 DIGIT SOLUTION")
# ######################################################################################################################

# set seed
r.seed(1)

# store the candidate arrays in a list
candidates_64 = []
# # # r.randint(0,2,64)) # # # for non-intelligent initialization

# create 10 candidates and store them in the list
for i in range(10):

    # create a blank "board"
    candidate_64 = np.zeros((8, 8), dtype=int)
    # # # candidate_64.reshape(64) # for "proper" genotype

    # "create new queens" on the "board" until you have 8 of them
    on_board = 0
    while on_board < 8:

        # create a random number 0-63
        cord_number = r.randint(0, 64, dtype=int)

        # use the mod and int_devision of that number as xy coordinates
        cord_x = int(cord_number / 8)
        cord_y = cord_number % 8

        # if that coordinate doesn't have a queen add it to the board
        if candidate_64[cord_x, cord_y] == 0:
            candidate_64[cord_x, cord_y] = 1
            on_board += 1

    # print the phenotype for the homework
    print(i)
    print(candidate_64)

    # add the candidate to the list
    candidates_64.append(candidate_64)

# now you have a list of 10 potential candidates (stored as arrays)
candidates_64 = np.array(candidates_64)

# ######################################################################################################################
print("8 DIGIT SOLUTION")
# ######################################################################################################################

# set seed
r.seed(1)

# store the candidate arrays in a list
candidates_8 = []

# create 10 candidates and store them in the list
for i in range(10):

    # create a blank solution
    candidate_8 = np.zeros(8, dtype=int)

    # add a random number 0-7 to the solution
    for j in range(8):
        candidate_8[j] = r.randint(0,8)

    # make a phenotype
    p_candidate_8 = np.zeros((8, 8), dtype=int)
    for j in range(8):
        p_candidate_8[j,candidate_8[j]] = 1

    # print the phenotype for the homework
    print(i)
    print(p_candidate_8)

    # add the candidate to the list
    candidates_8.append(candidate_8)


# print genotypes for homework
for i in range(len(candidates_8)):
    print(candidates_8[i])

# now you have a list of potential candidates
candidates_8 = np.array(candidates_8)

# # # another 8-digit solution would be to make 8 random numbers be the positions of the queens
# like if the board was numberd from left-to-right top-to-bottom (/8 and %8 for phenotype coordinates)
