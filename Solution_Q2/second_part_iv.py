# -*- coding: utf-8 -*-
"""q2part4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fPRahf-Iw0bEQUydDRUwTEC-fb5DqPhf
"""



# -*- coding: utf-8 -*-
"""q2part3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1OGdT23YHlU2NpbEn5HuWbHBVuxghV6NF
"""

# -*- coding: utf-8 -*-

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

#kernel matrix
X_new = data - data.mean(axis=0)
K=np.zeros((1000,1000))
for i in range (1000):
  for j in range (1000):
    answer=np.dot(X_new[i].T,X_new[j])
    K[i][j]=(1+answer)*(1+answer)*(1+answer)

def kernelexp(sigma):
  X_new = data - data.mean(axis=0)
  k=np.zeros((1000,1000))
  for i in range (1000):
    for j in range (1000):
      temp=X_new[i,:]-X_new[j,:]
      answer=np.dot(temp,temp.T)
      answer=-answer
      answer=answer/(2.0*sigma*sigma)
      final=np.exp(answer)
      k[i][j]=final
  return k

#make K matrix for different kernel functions
K=kernelexp(0.5)
#print (K)

# centre the H matrix
# by pre and post multiplication
a=np.eye(1000,1000)
b=np.ones((1000,1000))
c=np.zeros((1000,1000))
c=np.dot(a-b/1000,K)
d=np.zeros((1000,1000))
K=np.dot(c,a-b/1000)
#print(K)

#take top 4 eigen vectors
w, v = np.linalg.eig(K)
idx = w.argsort()[::-1]   
w = w[idx]
v = v[:,idx]
#print(v[0])

#V=np.array([v[:,0],v[:,1],v[:,2],v[:,3]])

#print (V)
#H=normalise L2 rows of V
#llyods on H
H=np.zeros((1000,4))
for i in range (4):
  for j in range(1000):
    H[j][i]=v[j][i]

import cmath
#V.shape
#print(H.shape)
for i in range(1000):
  sum=0
  for j in range (4):
    sum+=(H[i][j])*(H[i][j])
  for j in range (4):
    H[i][j]=H[i][j]/cmath.sqrt(sum)

def llyod(k,data,points):
  #take an array of 1000
  #A = np.random.randint(k, size=(1000))
  A=[0 for i in range(1000)]

#assigning on basis of arg max
  for i in range (1000):
    max=float('-inf')
    for j in range (4):
      if H[i][j] > max:
        max = H[i][j]
        index = j
    A[i]=index


  #function for error
  def errorcalculate():
    errsum=0
    mean=meanfunction(data,A)
    for i in range (1000):
      errsum+=np.linalg.norm(data[i]-mean[A[i]])**2
    return errsum

  def meanfunction(data,A):
    centroids=[]
    for i in range (k):
      count=0
      sum=0
      for j in range (1000):
        if(A[j]==i) :
          sum=sum+data[j]
          count+=1
        #mean=data.mean(axis=0)
      centroids.append(sum/count)
    return centroids

  #re-initialization if applicable 
  def reinit(A):
    flag=0
    mean=meanfunction(data,A)
    for i in range (1000):
      min=np.linalg.norm(data[i]-mean[A[i]])**2
      cluster=A[i]
      for j in range(k):
        dist=(np.linalg.norm(data[i]- mean[j]))**2
        if (dist<min):
          min=dist
          flag=1
          cluster=j
      A[i]=cluster
    return flag



  #find means
  #reinitailcie till flag==0
  err=[]
  flag=1
  while(True):
    flag=reinit(A)
    err.append(errorcalculate())
    if(flag==0):
      break
  ans=meanfunction(data,A)
  

  #draw after changes
  import matplotlib.pyplot as plt
  plt.xlabel("Dimension 1")
  plt.ylabel("Dimension 2")
  plt.title(" Data")
  for i in range(1000):
    if (A[i]==0):
      plt.scatter(points[i][0],points[i][1],color = 'red')
    if (A[i]==1):
      plt.scatter(points[i][0],points[i][1],color = 'blue')
    if (A[i]==2):
      plt.scatter(points[i][0],points[i][1],color = 'green')
    if (A[i]==3):
      plt.scatter(points[i][0],points[i][1],color = 'yellow')

  plt.show()
  return(ans)

#clustering on V for k=4
#after using arg max to map eigen vectors to clusters 
answer=llyod(4,H,data)