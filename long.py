# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 09:02:27 2019

@author: theresh
"""

import numpy as np

h1=np.array([1,1,1,0,1,0,0])
h2=np.array([1,0,1,1,0,1,0])
h3=np.array([1,1,0,1,0,0,1])
H=np.vstack((h1,h2,h3))
ht=H[:,np.array([0,1,2,3])]
L=np.zeros((3,7))
Eb_N0_dB=1
Eb=7/4.0
N0 = Eb/(np.exp(Eb_N0_dB*np.log(10)/10.0))
noise=np.random.normal(0,np.sqrt(N0/2.0),(7,))
ip=np.random.randint(0,2,4)
p=np.matmul(ht,ip)%2
c=np.concatenate((ip,p))
xc=1-2*c
rx=xc+noise
print rx

def decoding(rx,H):
    for iteration in range(10):
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
        #print beta
        sortarr=np.sort(beta)
        R=np.zeros((3,7))

for iteration in range(10):
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
    #print beta
    sortarr=np.sort(beta)
    R=np.zeros((3,7))
    for i in range(3):
        min_pos1=np.argmin(beta[i])
        #print min_pos1
        min2=sortarr[i][1]
        #print min2
        for j in range(4):
            #print j
            if (j!=min_pos1):
                R[i][y[i][j]]=np.prod(alpha[i])*alpha[i][j]*beta[i][min_pos1]
            else:
                R[i][y[i][j]]=np.prod(alpha[i])*alpha[i][j]*min2
    rx1=np.vstack((R,rx))
    rx_new=np.sum(rx1,axis=0)
    rx=rx_new
    print rx

chat=1*(rx<0)
error=(c[0:4]!=chat[0:4]).sum()
print error
    
                
            
#for i in range(3):
#    for j in range(7):
#        if(H[i][j]==1):
#            L[i][j]=rx[j]
#          
#x,y=np.nonzero(L)
#y=np.reshape(y,(3,4))
#D=rx[y]
##print D
#alpha=np.sign(D)
##print alpha
#beta=np.abs(D)
##print beta
#sortarr=np.sort(beta)
#R=np.zeros((3,7))
#for i in range(3):
#    min_pos1=np.argmin(beta[i])
#    #print min_pos1
#    min2=sortarr[i][1]
#    #print min2
#    for j in range(4):
#        #print j
#        if (j!=min_pos1):
#            R[i][y[i][j]]=np.prod(alpha[i])*alpha[i][j]*beta[i][min_pos1]
#        else:
#            R[i][y[i][j]]=np.prod(alpha[i])*alpha[i][j]*min2
#rx1=np.vstack((R,rx))
#rx_new=np.sum(rx1,axis=0)
#chat=1*(rx_new<0)
#error=(chat[0:4]!=c[0:4]).sum()
#print c
#print chat
#print error