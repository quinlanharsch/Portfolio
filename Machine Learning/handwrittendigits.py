#libraries
import os
import numpy as np
import pandas as pd
from sklearn.metrics import confusion_matrix
from sklearn.preprocessing import LabelBinarizer
import keras
from keras.models import Sequential
from keras.layers import Dense
import matplotlib.pyplot as plt
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


# seed rng
np.random.seed(3520)

#load data
testingdata = load_images('t10k-images.idx3-ubyte')
testinglabels = load_labels('t10k-labels.idx1-ubyte')
trainingdata = load_images('train-images.idx3-ubyte')
traininglabels = load_labels('train-labels.idx1-ubyte')

#X train

X = trainingdata/255.0
X = X.reshape((784,60000))
X = np.swapaxes(X,0,1)

#Y train

Y = traininglabels
encoder = LabelBinarizer()
T = encoder.fit_transform(Y) #makes one hot target

#X train

testX = trainingdata/255.0
testX = testX.reshape((784,60000))
testX = np.swapaxes(testX,0,1)

#Y train

testY = traininglabels
testT = encoder.fit_transform(testY) #makes one hot target

#relevant parameters
num_samples = 60000
batch_size = 100 # Samples/batch-size updates to get an epoch (50*3)
epochs = 100
learning_rate = 0.02

#Create nnet
#model = Sequential()
#model.add(Dense(units=300, activation='sigmoid', input_dim=784))
#model.add(Dense(units=10,activation='sigmoid'))
#model.summary()
model = Sequential()
model.add(Dense(units=300, activation='relu', input_dim=784))
model.add(Dense(units=300, activation='relu'))
model.add(Dense(units=10,activation='softmax'))
model.summary()

sgd = keras.optimizers.SGD(lr=learning_rate)
model.compile(loss='mean_squared_error', optimizer=sgd, metrics=['accuracy'])

#train
hx = model.fit(
    X, T,
    batch_size=batch_size,
    epochs=epochs,
    verbose=2,
    validation_data=(testX,testT)
)

score = model.evaluate(X, T, verbose=0)
print("Test loss: ", score[0])
print("Test accuracy: ", score[1])

print(confusion_matrix(model.predict(X).argmax(axis=-1), testY))

#plot history (hx)
print(hx.history.keys())
plt.figure(1)

#plot (from
plt.plot(hx.history['acc'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')

plt.show()