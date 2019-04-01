# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 17:00:23 2019

@author: theresh
"""

import numpy as np

h1=np.array([1,1,1,0,1,0,0])
h2=np.array([1,0,1,1,0,1,0])
h3=np.array([1,1,0,1,0,0,1])
H=np.vstack((h1,h2,h3))
L=np.zeros((3,7))

rx=np.array([ -1.34416543,  1.72663299, -0.71026459,  1.13644959,  1.15528483,
        0.78103986, -0.85093872])
ip=np.random.randint(0,2,4)

for i in range(3):
    for j in range(7):
        if(H[i][j]==1):
            L[i][j]=rx[j]
          
x,y=np.nonzero(L)
y=np.reshape(y,(3,4))
###array([1, 0, 1, 0, 0, 0, 1])

D=rx[y]
print D
alpha=np.sign(D)
print alpha
beta=np.abs(D)
print beta
sortarr=np.sort(beta)
R=np.zeros((3,7))
for i in range(3):
    min_pos1=np.argmin(beta[i])
    print min_pos1
    min2=sortarr[i][1]
    print min2
    for j in range(4):
        #print j
        if (j!=min_pos1):
            R[i][y[i][j]]=np.prod(alpha[i])*alpha[i][j]*beta[i][min_pos1]
        else:
            R[i][y[i][j]]=np.prod(alpha[i])*alpha[i][j]*min2
rx1=np.vstack((R,rx))
rx_new=np.sum(rx1,axis=0)
chat=1*(rx_new<0)


        