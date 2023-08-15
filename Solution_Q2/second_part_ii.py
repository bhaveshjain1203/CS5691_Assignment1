from ast import MatMult
from tkinter import font
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math
import random
import sys

WS=pd.read_csv('Dataset.csv' ,header=None,index_col=False)

# then convert it to numpy 2darray
data =np.array(WS)
#print(data)
colours={0:'red',1:'blue',2:'yellow',3:'orchid',4:'green'}
#take an array of 1000
def randominit(k):
    A = np.random.randint(k, size=(1000))
    return A
#function for error
def errorcalculate(A,k):
  errsum=0
  mean=meanfunction(data,A,k)
  for i in range (1000):
    errsum+=np.linalg.norm(data[i]-mean[A[i]])**2
  return errsum

def meanfunction(data,A,k):
  #return centroid
  centroids=[]
  for i in range (k):
    count=0
    sum=0
    for j in range (1000):
      if(A[j]==i) :
        sum=sum+data[j]
        count+=1
      #mean=data.mean(axis=0)
    if(count!=0):
        centroids.append(sum/count)
    else:
        centroids.append(0)
  return centroids

#re-initialization if applicable 
def reinit(A,k):
  flag=0
  mean=meanfunction(data,A,k)
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
  return flag,mean

def voronoi(A,k,mean):
    f3=plt.figure(3)
    i=-10
    z=0
    while(i<11):
        j=-10
        while(j<11):
            min=sys.maxsize
            for l in range(k):
                x=mean[l][0]
                y=mean[l][1]
                if (math.sqrt(((i-x)**2)+((j-y)**2))<min):
                    min=math.sqrt(((i-x)**2)+((j-y)**2))
                    z=l
            plt.xlabel("X-axis")
            plt.ylabel("Y-axis")
            plt.title("Voronoi Regions")
            plt.scatter(i,j,c=colours[z])
            j+=0.5
        i+=0.5
    plt.show()


#driver function
def mainfunction(k,A):
    for i in range(1000):
        A[i]=A[i]%k
    err=[]
    flag=1
    while(True):
        flag,mean=reinit(A,k)
        err.append(errorcalculate(A,k))
        if(flag==0):
            break
    voronoi(A,k,mean)
    plotting(A,k)
    y=len(err)
    z=[]
    for i in range(y):
        z.append(i)
    
    plt.plot(z,err,'-ok')
    plt.xlabel("Iteration number")
    plt.ylabel("Error Value")
    plt.title("Error Function Vs Iteration")
    plt.show()
def plotting(A,k):
#draw after changes
    import matplotlib.pyplot as plt
    plt.xlabel("Dimension 1")
    plt.ylabel("Dimension 2")
    plt.title("K Means")
    for i in range(1000):
        for j in range(k):
            if (A[i]==j):
                plt.scatter(data[i][0],data[i][1],color = colours[j])

    plt.show()
k=5
A=randominit(k)
for i in range(2,6):
    mainfunction(i,A)