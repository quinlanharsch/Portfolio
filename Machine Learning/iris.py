#libraries
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelBinarizer
import keras
from keras.models import Sequential
from keras.layers import Dense

# seed rng
np.random.seed(3520)

#load data
dataframe = pd.read_csv("iris.csv",header=None)
dataset = dataframe.values

#XY
X = dataset[:,:4].astype('float32')
Y = dataset[:,4]

#T
encoder = LabelBinarizer()
T = encoder.fit_transform(Y) #makes one hot target

#relevant parameters
num_samples, num_inputs = X.shape
num_outputs = len(np.unique(Y))
batch_size = 50 # Samples/batch-size updates to get an epoch (50*3)
epochs = 1000
learning_rate = 0.01

#Create nnet
model = Sequential()
model.add(Dense(units=100, activation='sigmoid', input_dim=num_inputs))
model.add(Dense(units=num_outputs,activation='sigmoid'))
model.summary()

sgd = keras.optimizers.SGD(lr=learning_rate)
model.compile(loss='mean_squared_error', optimizer=sgd, metrics=['accuracy'])

#train
model.fit(
    X, T,
    batch_size=batch_size,
    epochs=epochs,
    verbose=2
)

score = model.evaluate(X, T, verbose=0)
print("Test loss: ", score[0])
print("Test accuracy: ", score[1])