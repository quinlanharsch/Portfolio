# knn.py
# Simple example of k-Nearest Neighbors machine learning algorithm.

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from scipy.spatial import Voronoi
from sklearn import neighbors
import random

## Set relevant parameters
seed = 4
num_samples = 10
num_classes = 3
labels = [1,1,0,0,2,0,1,2,2,2]
#[1,1,0,0,2,0,1,2,1,2]
k = 1 # how many nearest neighbors to use?

x1_min, x1_max = -0.1, 1.1 # x1 bounds for meshgrid
x2_min, x2_max = -0.1, 1.1 # x2 bounds for meshgrid
h = 0.002 # step size of mesh

cmap_light = ListedColormap(['#FFAFAF','#AFAFFF','#F6D587'])
cmap_bold = ListedColormap(['red','blue','orange'])

## Generate random data
np.random.seed(seed)
X = np.random.rand(num_samples, 2)
if 'labels' in locals() and len(labels)==num_samples:
    Y = labels
else:
    Y = random.choices(range(num_classes), k=num_samples)

## Run k-NN
clf = neighbors.KNeighborsClassifier(k, weights='uniform')
clf.fit(X,Y)

## Plot results
plt.figure(1)
plt.clf()

# Make decision boundary
xx, yy = np.meshgrid(
    np.arange(x1_min, x1_max, h),
    np.arange(x2_min, x2_max, h))
Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)
plt.pcolormesh(xx, yy, Z, cmap=cmap_light, alpha=1)

# Plot training data
plt.scatter(X[:, 0], X[:, 1], c=Y,
    cmap=cmap_bold,
    edgecolor='k',
    s=100)
plt.xlim(xx.min(), xx.max())
plt.ylim(yy.min(), yy.max())

# Edit plot properties
plt.title("{}-class k-nearest neighbors classification (k = {})".format(num_classes,k))
plt.xlabel('x1')
plt.ylabel('x2')
plt.show()
