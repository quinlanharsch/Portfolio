#libraries
import numpy as np
import matplotlib.pyplot as plt
from sklearn import neighbors
import random as rng
from skimage.util import montage

def load_images(filename):
    with open(filename, 'rb') as fid:
        # Read magic number
        magic = np.fromfile(fid, '>i4', 1)
        assert magic[0] == 2051, "Bad magic number in {} (expected 2051, but got {})".format(filename, magic[0])

        # Read number and size of images
        num_images = np.fromfile(fid, '>i4', 1)
        num_rows = np.fromfile(fid, '>i4', 1)
        num_cols = np.fromfile(fid, '>i4', 1)

        # Read image data
        images = np.fromfile(fid, '>u1').reshape((num_images[0], num_rows[0], num_cols[0])).transpose((1, 2, 0))
        return images


def load_labels(filename):
    with open(filename, 'rb') as fid:
        # Read magic number
        magic = np.fromfile(fid, '>i4', 1)
        assert magic[0] == 2049, "Bad magic number in {} (expected 2049, but got {})".format(filename, magic[0])

        # Read number and size of images
        num_images = np.fromfile(fid, '>i4', 1)

        # Read image data
        labels = np.fromfile(fid, '>u1').reshape((num_images[0], -1))
        return labels


def show_images(images, N=1, shape=None):
    # Show N random samples from the dataset.
    ind = np.random.choice(images.shape[2], N, replace=False)
    ind.shape = (len(ind),)

    if shape is None:
        s = int(np.ceil(N**(0.5)))
        shape = (s, s)
    m = montage(images[:, :, ind].transpose(2, 0, 1), grid_shape=shape)
    plt.imshow(m, cmap='gray')
    plt.axis('off')
    plt.show()


''' '' '' '' '' '' '' '' '' '' '' '' '' '' '' '' '' '' '' '' ''
Set relevant model parameters
''' '' '' '' '' '' '' '' '' '' '' '' '' '' '' '' '' '' '' '' ''
seed = 4
num_samples = 60000
num_classes = 10
k = 1# how many nearest neighbors to use?
''' '' '' '' '' '' '' '' '' '' '' '' '' '' '' '' '' '' '' '''
print(f"k: {k}")


# load data
testingdata = load_images('t10k-images.idx3-ubyte')
testinglabels = load_labels('t10k-labels.idx1-ubyte')
trainingdata = load_images('train-images.idx3-ubyte')
traininglabels = load_labels('train-labels.idx1-ubyte')

# X train

X = trainingdata/255.0
X = X.reshape((784,-1)).T

Xtest = testingdata/255.0
Xtest = Xtest.reshape((784,-1)).T
Xtest = Xtest[:100, :]


# Y train

Y = traininglabels
Y = Y[:,0]

Ytest = testinglabels
Ytest = Ytest[:,0]
Ytest = Ytest[:100]

# Run k-NN
clf = neighbors.KNeighborsClassifier(k)
clf.fit(X,Y)
Ypred = clf.predict(Xtest)

# Accuracy
print(f"Accurcy: {clf.score(Xtest, Ytest)}")

#Problem 2 b
misclass = np.where(Ypred != Ytest)[0][0]

plt.imshow(testingdata[:,:, misclass], cmap='gray')
plt.waitforbuttonpress()

dist, cord = clf.kneighbors([Xtest[misclass]], k+1) # returns a really dumb looking np array
cord = cord[0].tolist()                             # fixes it

for i in cord:
    plt.imshow(trainingdata[:,:,i], cmap='gray')
    plt.waitforbuttonpress()