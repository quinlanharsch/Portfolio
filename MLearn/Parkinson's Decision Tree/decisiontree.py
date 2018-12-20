# decisiontree.py
# Predict Parkinson's disease based on dysphonia measurements using a decision tree.

import os
import numpy as np
from sklearn import tree
from sklearn.metrics import confusion_matrix
import graphviz

# Relevant directories and filenames
root = '~/Documents/csc3520/assignments/hw2' #edit as needed

# Load data from relevant files
attributesArray = np.loadtxt("attributes.txt", dtype=str)
trainingDataArray = np.loadtxt("trainingdata.txt", dtype=float, delimiter=',')
trainingLabelArray = np.loadtxt("traininglabels.txt", dtype=int)
testingDataArray = np.loadtxt("testingdata.txt", dtype=float ,delimiter=',')
testingLabelsArray = np.loadtxt("testinglabels.txt", dtype=int)

# Train a decision tree via information gain on the training data
clf = tree.DecisionTreeClassifier(criterion="entropy")
clf = clf.fit(trainingDataArray, trainingLabelArray)

# Test the decision tree
clfTestingLabelsArray = clf.predict(testingDataArray)

# Compute the confusion matrix on test data
print(clf.score(testingDataArray, testingLabelsArray))
print(confusion_matrix(testingLabelsArray, clfTestingLabelsArray))

# Visualize the tree using graphviz
os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'
dot_data = tree.export_graphviz(clf, out_file=None, feature_names=attributesArray, class_names=["Healthy", "Parkinsons"], filled=True, rounded=True)
graph = graphviz.Source(dot_data)
graph.render("parkinsons")