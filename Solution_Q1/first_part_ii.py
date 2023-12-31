# -*- coding: utf-8 -*-
"""firstopartii.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kRAYXmB4-Df4ymczM4lWHe0WNENjKQRx
"""

#upload the file
import numpy as np
import pandas as pd
import io
from google.colab import files 
uploaded = files.upload()

# then convert data from the file to 2d array
with open('Dataset.csv') as csvfile:
      data =np.loadtxt(csvfile, delimiter=",")
#print(data)

import matplotlib.pyplot as plt

plt.figure(1)
plt.scatter(data[:,0],data[:,1])
plt.xlabel("Dimension 1")
plt.ylabel("Dimension 2")
plt.title("Original Data")
plt.show()

# caclucalte the covariance matrix 
covmatrix = np.dot(data.T,data)/1000
print("Covariance Matrix")
for z in covmatrix:
   print(z)

# find the eigen value and vector use inbuilt lib for this 
w, v = np.linalg.eig(covmatrix)
print('E-value:', w)
print('E-vector', v)

# project the data to the eigen vector
# centred data matrix dot eigen vector
row,column=v.shape
sumofeigenvalues=w[0]+w[1]
for i in range(row):
  variance=w[i]/sumofeigenvalues
  print("Variance",i+1,"(along Principal Component",i+1,")","=",variance)

resultnew = np.dot(data,v)
for i in v:
  plt.scatter(resultnew[:,1],resultnew[:,0],zorder=1)
plt.xlabel("PrincipalComponent 1")
plt.ylabel("PrincipalComponent 2")
plt.title("Principal Component Analysis")
plt.show()