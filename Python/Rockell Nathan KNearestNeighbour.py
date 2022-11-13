import numpy as np
import pandas as pd
import csv
from csv import writer
import os

#Maths Libraries
import matplotlib.pyplot as plt
from scipy.fft import fft, ifft, fftfreq
import statistics

#Machine Learning Libraries
import sklearn
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
import tensorflow as tf
import keras
from sklearn.preprocessing import StandardScaler 
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix

activity = ['standing', 'sitting', 'walking', 'jogging', 'running', 'cycling']

def KNearestNeightbourTrain(k):
    
    # Convert dataset to a pandas dataframe:
    dataset = readInData("")

    classifier = KNeighborsClassifier(n_neighbors=k)

    # Assign values to the X and y variables:
    X = dataset.iloc[:, 1:].values
    y = dataset.iloc[:, 0].values 

    # print('Data Values:', X)
    # print('Activity Labels: ', y)

    # # Split dataset into random train and test subsets:
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2) 

    # # Standardize features by removing mean and scaling to unit variance:
    scaler = StandardScaler()
    scaler.fit(X_train)

    X_train = scaler.transform(X_train)
    X_test = scaler.transform(X_test) 

    # # Use the KNN classifier to fit data:
    classifier.fit(X_train, y_train) 

    import seaborn as sns

    # # Predict y data with classifier: 
    y_predict = classifier.predict(X_test)
    cf_matrix = confusion_matrix(y_test, y_predict)

    sns.set(rc = {'figure.figsize':(10, 10)})
    ax = sns.heatmap(cf_matrix, annot=True, cmap='Blues')

    ax.set_title('Confusion Matrix with labels\n');
    ax.set_xlabel('\nPredicted Values')
    ax.set_ylabel('Actual Values ');

    ## Ticket labels - List must be in alphabetical order
    ax.xaxis.set_ticklabels(activity)
    ax.yaxis.set_ticklabels(activity)

    ## Display the visualization of the Confusion Matrix.
    plt.show()

    # A = classifier.kneighbors_graph(X_train)
    # A.toarray()
    # print(A)

    ## Print results: 
    print(confusion_matrix(y_test, y_predict))
    print(classification_report(y_test, y_predict)) 