# -*- coding: utf-8 -*-
"""

Author: Nathan Rockell
#Smartphone-based recognition of human activities. Using KNN machine learning to predict the activity a user has performed, 
using mathematically calculated values with data from the accelerometer.
"""

"""### Libraries"""

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

"""## Global Variables"""

#Length of time each recording is
recordingLength = 20
#How many values are captured per second
recordingsPerSecond = 0.25
#Activity Array
activity = ['standing', 'sitting', 'walking', 'jogging', 'running', 'cycling']

"""## Data Preprocessing"""

def portionData(length, array):
  a = array
  portionSize = int(length)
  #Portions the data within the array to set size of 80 values, which is 20 seconds
  a_portions = [a[x:x+portionSize] for x in range(0, len(a.astype(int)), portionSize)]
  print('Data Portioned')
  return a_portions

"""## Maths Analysis

### FFT Function
"""

def runFFT(x, y, z):
    #Length of array 
    N = len(x)
    #Timeframe
    T = len(x)*recordingsPerSecond
    
    t = np.linspace(0, T, N)
    f = fftfreq(len(t), np.diff(t)[0])
    #Calculates FFT values for each axis
    xfft = fft(x)
    yfft = fft(y)
    zfft = fft(z) 
    # print('fft:', (xfft))
    plt.plot(t, x, label="Accel X")
    plt.plot(t, y, label="Accel Y")
    plt.plot(t, z, label="Accel Z")
    plt.legend(loc="upper right")
    plt.xlabel('t [seconds]')
    plt.ylabel('Accelerometer Value')
    plt.show()
    
    plt.plot(f[:N//2], np.abs(xfft[:N//2]), label ="Accel X FFT")
    plt.legend(loc="upper right")
    # plt.show()
    plt.plot(f[:N//2], np.abs(yfft[:N//2]), label ="Accel Y FFT")
    plt.legend(loc="upper right")
    # plt.show()
    plt.plot(f[:N//2], np.abs(zfft[:N//2]), label ="Accel Z FFT")
    plt.legend(loc="upper right")
    plt.ylabel('Frequency')
    plt.xlabel('')
    # plt.show()
    print(xfft[0])
    print("FFT Values Calculated")
    return xfft[0], yfft[0], zfft[0]

"""### Mean

"""

def mean(arrayX, arrayY, arrayZ):
  mean_x = statistics.mean(arrayX)
  mean_y = statistics.mean(arrayY)
  mean_z = statistics.mean(arrayZ)
  print("Mean Values Calculated")
  return mean_x, mean_y, mean_z

"""### Standard Deviation"""

def stdev(arrayX, arrayY, arrayZ):
  stdev_x = statistics.stdev(arrayX)
  stdev_y = statistics.stdev(arrayY)
  stdev_z = statistics.stdev(arrayZ)
  print("Standard Deviation Values Calculated")
  return stdev_x, stdev_y, stdev_z

"""### Variance"""

def variance(arrayX, arrayY, arrayZ):
  vari_x = statistics.variance(arrayX)
  vari_y = statistics.variance(arrayY)
  vari_z = statistics.variance(arrayZ)
  print("Variance Values Calculated")
  if(vari_x == 'nan'):
    vari_x = 0
  if(vari_y == 'nan'):
    vari_y = 0
  if(vari_z == 'nan'):
    vari_z = 0
  return vari_x, vari_y, vari_z

"""### Max & Min"""

def maxNum(arrayX, arrayY, arrayZ):
  max_x = max(arrayX)
  max_y = max(arrayY) 
  max_z = max(arrayZ)
  print("Max Value Calculated")
  return max_x, max_y, max_z

def minNum(arrayX, arrayY, arrayZ):
  min_x = min(arrayX)
  min_y = min(arrayY) 
  min_z = min(arrayZ)
  print("Min Value Calculated")
  return min_x, min_y, min_z

"""##Reading and Writing Data Functions"""

def readInData(filepath):
  dataset = pd.read_csv(filepath)
  print("Dataset Read")
  return dataset

def writeToCsv(filepath, data):
  f = open(filepath, 'a')
  writer = csv.writer(f)
  
  writer.writerow(data)
  print('Data Written To CSV')
  f.close()

"""##Calculating Rows Function"""

def calculateMathAnalysis(data_path, activity, accel_x, accel_y, accel_z):
  data = []
  print('Calculating Rows')
  length = len(accel_x)
  if(length <= 1):
    length = 1
  else:
    length-=1

  for i in range(10):
    fftx, ffty, fftz = runFFT(accel_x[i], accel_y[i], accel_z[i])
    mx, my, mz = mean(accel_x[i], accel_y[i], accel_z[i])
    stdx, stdy, stdz = stdev(accel_x[i], accel_y[i], accel_z[i])
    varx, vary, varz = variance(accel_x[i], accel_y[i], accel_z[i])
    mxx, mxy, mxz = maxNum(accel_x[i], accel_y[i], accel_z[i])
    mnx, mny, mnz = minNum(accel_x[i], accel_y[i], accel_z[i])
    
    data.append(activity)
    arr = np.array(fftx)
    arr = str(arr).lstrip('(').rstrip('-0j)')
    data.append(float(arr))
    arr = np.array(ffty)
    arr = str(arr).lstrip('(').rstrip('-0j)')
    data.append(float(arr))
    arr = np.array(fftz)
    arr = str(arr).lstrip('(').rstrip('-0j)')
    data.append(float(arr))

    data.append(mx)
    data.append(my)
    data.append(mz)

    data.append(stdx)
    data.append(stdy)
    data.append(stdz)

    data.append(varx)
    data.append(vary)
    data.append(varz)

    data.append(mxx)
    data.append(mxy)
    data.append(mxz)

    data.append(mnx)
    data.append(mny)
    data.append(mnz)
    writeToCsv(data_path, data)
    data = []

def BuildCSVFile(data_path, activity, x,y,z):
  #Portions the data into separate arrays of set length
  accel_x = portionData(recordingLength/recordingsPerSecond, x)
  accel_y = portionData(recordingLength/recordingsPerSecond, y)
  accel_z = portionData(recordingLength/recordingsPerSecond, z)
  #Runs through each maths analysis and appends the row to the data csv file
  calculateMathAnalysis(data_path, activity, accel_x, accel_y, accel_z)

"""##Main Function

CSV File Rows: 
activity, fftx, ffty, fftz, mx, my, mz, stdx, stdy,stdz, varx, vary, varz, mxx, mxy, mxz, mnx, mny, mnz
"""

def main():
  data_path = '/Data'
  file_path = '/activityData.csv'

  for i in activity:
    print('**********')
    accel_x = np.loadtxt(data_path+'/'+i+'_x.csv', dtype=float)
    accel_y = np.loadtxt(data_path+'/'+i+'_y.csv', dtype=float)
    accel_z = np.loadtxt(data_path+'/'+i+'_z.csv', dtype=float)
    
    BuildCSVFile(file_path, i, accel_x, accel_y, accel_z)
    print('**********')
main()

# data_path = '/content/drive/MyDrive/Smartphone-based Recognition/Data'
# accel_x = np.loadtxt(data_path+'/running_x.csv', dtype=float)
# accel_y = np.loadtxt(data_path+'/running_y.csv', dtype=float)
# accel_z = np.loadtxt(data_path+'/running_z.csv', dtype=float)
# x = portionData(80, accel_x)
# y = portionData(80, accel_y)
# z = portionData(80, accel_z)
# runFFT(x[1], y[1] ,z[1])

activityData = readInData('/activityData.csv')
activityData.head(20)

"""## Machine Learning Algorithm"""

def KNearestNeightbourTrain(k):
  # Convert dataset to a pandas dataframe:
  dataset = readInData("/activityData.csv")

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

KNearestNeightbourTrain(2)