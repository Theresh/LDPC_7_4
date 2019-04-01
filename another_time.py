# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 11:14:26 2019

@author: theresh
"""

import numpy as np
#Eb_N0_dB=3
#print Eb_N0_dB
h1=np.array([1,1,1,0,1,0,0])
h2=np.array([1,0,1,1,0,1,0])
h3=np.array([1,1,0,1,0,0,1])
H=np.vstack((h1,h2,h3))
#print H
ht=H[:,np.array([0,1,2,3])]

Eb=7/4.0
#N0 = Eb/(np.exp(Eb_N0_dB*np.log(10)/10.0))
#noise=np.random.normal(0,np.sqrt(N0/2.0),7)
noise=np.array([ 0.87140519,  0.32848601,  0.26282904,  0.65793898, -1.47794962,
        0.80660831, -1.67639514])

#data=np.random.randint(0,2,4)
data=np.array([0,1,1,0])
#p=np.matmul(ht,data)%2
p=np.array([0,1,1])

#ip=np.concatenate((data,p))
ip=np.array([0,1,1,0,0,1,1])
c=1-2*ip
#c=
print ip
print c

rx=ip+noise

print rx
L=np.zeros((3,7))
for i in range(3):
    for j in range(7):
        if(H[i][j]==1):
            L[i][j]=rx[j]
x,y=np.nonzero(L)
y=np.reshape(y,(3,4))
D=rx[y]
#print D
alpha=np.sign(D)
#print alpha
beta=np.abs(D)

R=np.zeros((3,7))
for i in range(3):
    sortarr=np.sort(beta)
    min_pos1=np.argmin(beta[i])
    #print min_pos1+
    min2=sortarr[i][1]
    #print min2
    for j in range(4):
        if (j!=min_pos1):
            R[i][y[i][j]]=np.prod(alpha[i])*alpha[i][j]*beta[i][min_pos1]
        else:
            R[i][y[i][j]]=np.prod(alpha[i])*alpha[i][j]*min2
rx1=np.vstack((R,rx))
rx_new=np.sum(rx1,axis=0)
print rx_new
rx=rx_new
L=np.zeros((3,7))
for i in range(3):
    for j in range(7):
        if(H[i][j]==1):
            L[i][j]=rx[j]
x,y=np.nonzero(L)
y=np.reshape(y,(3,4))
D=rx[y]
#print D
alpha=np.sign(D)
#print alpha
beta=np.abs(D)

R=np.zeros((3,7))
for i in range(3):
    sortarr=np.sort(beta)
    min_pos1=np.argmin(beta[i])
    #print min_pos1+
    min2=sortarr[i][1]
    #print min2
    for j in range(4):
        if (j!=min_pos1):
            R[i][y[i][j]]=np.prod(alpha[i])*alpha[i][j]*beta[i][min_pos1]
        else:
            R[i][y[i][j]]=np.prod(alpha[i])*alpha[i][j]*min2
rx1=np.vstack((R,rx))
rx_new=np.sum(rx1,axis=0)
print rx_new




