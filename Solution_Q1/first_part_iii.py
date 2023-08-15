# -*- coding: utf-8 -*-
"""firstpart3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15JUIcV51hCCZfCNmpVtuhytAeT9Tbfpf
"""

import numpy as np
import pandas as pd
import io
import cmath
import matplotlib.pyplot as plt
# get dataset from the file 

from google.colab import files 
uploaded = files.upload()

# then convert it to numpy 2darray
with open('Dataset.csv') as csvfile:
      data =np.loadtxt(csvfile, delimiter=",")
#print(data)

#kernel polynomial square matrix
def kernelsquare():
  X_new = data - data.mean(axis=0)
  k=np.zeros((1000,1000))
  for i in range (1000):
    for j in range (1000):
      answer=np.dot(X_new[i].T,X_new[j])
      k[i][j]=(1+answer)*(1+answer)
  return k

#kernel polynomial cube matrix
def kernelcube():
  X_new = data - data.mean(axis=0)
  k=np.zeros((1000,1000))
  for i in range (1000):
    for j in range (1000):
      answer=np.dot(X_new[i].T,X_new[j])
      k[i][j]=(1+answer)*(1+answer)*(1+answer)
  return k

#kernel exponential matrix
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

def plotkernelpca(k):
  #centre the kernel matrix
  #pre multiply & post multiply k by i-1/1000
  a=np.eye(1000,1000)
  b=np.ones((1000,1000))
  c=np.zeros((1000,1000))
  c=np.dot(a-b/1000,k)
  d=np.zeros((1000,1000))
  d=np.dot(c,a-b/1000)

  #find eigen values and eigen vectors

  w, v = np.linalg.eig(d)
  #print('E-value:', w)


  #take 2 eval and 2 eigen vector
  #multiply with X_newroot 
  #eigen vector=1/root (eigen value)
  lamda1=w[0]
  lamda2=w[1]

  beta1=v[:,0]
  beta2=v[:,1]

  alpha1=beta1/cmath.sqrt(lamda1)
  alpha2=beta2/cmath.sqrt(lamda2)

  alpha=np.matrix([alpha1,alpha2])

  answer=np.dot(d,alpha.T)
  #print(ans1)


  df = pd.DataFrame(answer,columns=['PrincipalComponent1','PrincipalComponent2'])
 
  import matplotlib.pyplot as plt
  df.plot(kind = 'scatter',
          x = 'PrincipalComponent1',
          y = 'PrincipalComponent2',
          color = 'red')
    
  # set the title
  plt.title('Kernel PCA')
  plt.grid()  
  # show the plot
  plt.show()

k=kernelsquare()
plotkernelpca(k)

k=kernelcube()
plotkernelpca(k)

sigma=0.1
k=kernelexp(sigma)
plotkernelpca(k)

sigma=0.2
k=kernelexp(sigma)
plotkernelpca(k)

sigma=0.3
k=kernelexp(sigma)
plotkernelpca(k)

sigma=0.4
k=kernelexp(sigma)
plotkernelpca(k)

sigma=0.5
k=kernelexp(sigma)
plotkernelpca(k)

sigma=0.6
k=kernelexp(sigma)
plotkernelpca(k)

sigma=0.7
k=kernelexp(sigma)
plotkernelpca(k)

sigma=0.8
k=kernelexp(sigma)
plotkernelpca(k)

sigma=0.9
k=kernelexp(sigma)
plotkernelpca(k)

sigma=1.0
k=kernelexp(sigma)
plotkernelpca(k)