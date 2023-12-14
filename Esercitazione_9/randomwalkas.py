import sys,os
import numpy as np 
import matplotlib.pyplot as plt 

def pf(phi):
    return 1/4*np.sin(0.5*phi)

#funzione cumulativa: c(x) = 1/2(1-cos(x/2))
def cf(phi):
    return 0.5 * (1-np.cos(0.5*phi))

def invcf(y):
    return 2 * np.arccos(1-2*y)


xx = np.arange(0, 2*np.pi, 0.1)
yy = np.arange(0, 1, 0.01)
y = np.random.random(100000)
phi = invcf(y)
    


fig, ax = plt.subplots(1, 2, figsize=(18,9))

ax[0].plot(xx,  pf(xx), color = 'orangered')
ax[0].set_xlabel('phi (rad)', fontsize = 20)
ax[0].set_ylabel('P')

ax[1].hist(phi, bins = 100, range=(0, 2*np.pi), color = 'royalblue')
ax[1].set_xlabel('phi (rad)', fontsize = 20)
ax[1].set_ylabel('N')

plt.show()