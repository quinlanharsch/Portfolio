# In class neural net

import numpy as np
import random as rand
import matplotlib.pyplot as plt

def sigmoid(x):
    return 1/(1.0 + np.exp(-x))


def linear(x):
    return x


def feedforward(X, Wij, Wjk):
    # forward propagate
    ###################

    bias = np.ones((X.shape[0], 1))

    # Aj = sum(Wij*Xi)
    Aj = np.dot(np.concatenate((bias,X),axis=1), Wij)

    # Zj = sigma j (Aj)
    Zj = sigmoid(Aj)

    # Ak = sum(Wjk*Zj)
    Ak = np.dot(np.concatenate((bias,Zj), axis=1), Wjk)

    # Y = sigma k (Ak)
    Y = linear(Ak)
    return Y, Zj


def backpropogate(X, i, Wij, Wjk, T, eta):
    # reverse propagate
    ###################

    # Extract Sample
    x = X[i,:]
    x.shape = (1,-1)

    t = T[i]

    # Feedforward to get neuron activations
    y, z = feedforward(x, Wij, Wjk)
    x.shape = (-1,1)
    z.shape = (-1,1)

    # Update hidden-to-output neurons
    wjk = Wjk - eta*(y - t)*np.vstack([1,z])

    # Update input-to-output neurons
    sens = - (y - t)*Wjk[1:]*(z*(1-z))
    wij = Wij + eta*sens.transpose()*np.vstack([1,x])

    # Return updated weights
    return wjk, wij


# Define sigma functions

# load data
X = np.array([
    [0,0],
    [1,2],
    [-1,2],
    [-2,-2],
    [3,0],
    [1, -3],
    [1, 3],
    [-3, -3],])
T = np.array([-1, -1, -1, -1, 1, 1, 1, 1])
T.shape = (-1, 1)

# load/generate weights

Wij = np.array([
    [rand.randint(0, 0), rand.randint(0, 0)],
    [rand.randint(0, 0), rand.randint(0, 0)],
    [rand.randint(0, 0), rand.randint(0, 0)],])
Wjk = np.array([rand.randint(0, 0), rand.randint(0, 0), rand.randint(0, 0)])
Wjk.shape = (-1, 1)

# learning parameters (eta)
eta = 0.2

# go forward
predicted, z = feedforward(X, Wij, Wjk)

backpropogate(X, 1, Wij, Wjk, T, eta)

# faltten to -1 or 1
Y = np.zeros(predicted.shape)
Y [predicted < 0] = -1
Y [predicted >= 0] = 1

# Calculate and print accuracy
accuracy = float(sum(T==Y)/float(len(T))*100.0)
print("Iteration 0: Accuracy: {:0.1f}".format(accuracy))

#Backpropogate the error

num_iter = 1000
accuracy = np.empty((num_iter, 1))
for i in range(num_iter):
    # Backpropagate the error
    ind = i % X.shape[0]  # which sample should we use
    Wij, Wjk = backpropogate(X, Wij, Wjk, T, ind, eta)

    # Recompute accuracy
    pred, Z = feedforward(X, Wij, Wjk)
    Y = np.zeros(pred.shape)
    Y[pred < 0] = -1
    Y[pred >= 0] = 1

    accuracy[i] = sum(T == Y) / len(T) * 100
    print('iter {} --> accuracy = {:0.1f}%'.format(i + 1, float(accuracy[i])))

plt.plot(accuracy)
plt.show()