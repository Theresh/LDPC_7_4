# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 15:06:36 2019

@author: theresh
"""

import numpy as np
from matplotlib import pyplot as plt



#===================================
# G= 1 0 0 0 1 1 1
#    0 1 0 0 1 0 1
#    0 0 1 0 1 1 0
#    0 0 0 1 0 1 1
# Systematic form 7,4 code gen matrix
#===================================

#Eb_N0_dB=np.linspace(0,8,5)
Eb_N0_dB=np.linspace(10,20,3)
#print Eb_N0_dB
h1=np.array([1,1,1,0,1,0,0])
h2=np.array([1,0,1,1,0,1,0])
h3=np.array([1,1,0,1,0,0,1])
H=np.vstack((h1,h2,h3))
#print H
ht=H[:,np.array([0,1,2,3])]
#print ht

Eb=7/4.0
frames=25000
 
def decoding(rx,H):
    max_iter=10
    for ite in range(max_iter):
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
        #print beta
        sortarr=np.sort(beta)
        R=np.zeros((3,7))
        for i in range(3):
            min_pos1=np.argmin(beta[i])
            #print min_pos1
            min2=sortarr[i][1]
            #print min2
            for j in range(4):
                if (j!=min_pos1):
                    R[i][y[i][j]]=np.prod(alpha[i])*alpha[i][j]*beta[i][min_pos1]
                else:
                    R[i][y[i][j]]=np.prod(alpha[i])*alpha[i][j]*min2
        rx1=np.vstack((R,rx))
        rx_new=np.sum(rx1,axis=0)
        rx=rx_new
    chat=1*(rx_new<0)
    return chat
sys_bit_error=np.zeros(len(Eb_N0_dB))
for i in range(len(Eb_N0_dB)):
    N0 = Eb/(10**(Eb_N0_dB[i]*0.1))
    noise=np.random.normal(0,np.sqrt(N0),(7,))
    error=0
    for fr in range(frames):
         ip=np.random.randint(0,2,4)
         #print ip
         p=np.matmul(ht,ip)%2
         #print p
         c=np.concatenate((ip,p))
         #print c
         xc=1-2*c
         rx=xc + noise
         #print rx,
         chat=decoding((2/N0)*rx,H)
         error=(c[0:4]!=chat[0:4]).sum()
         sys_bit_error[i]=sys_bit_error[i]+error
  
sys=sys_bit_error/(frames*4.0)
plt.semilogy(Eb_N0_dB,sys)
plt.grid(True)
plt.show()
