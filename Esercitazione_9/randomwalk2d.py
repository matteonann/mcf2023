import sys,os
import numpy as np 
import matplotlib.pyplot as plt 

def random_walk2d(s, N):
    deltax = np.array([0])
    deltay = np.array([0])
    x = 0
    y = 0
    check = np.random.uniform(0, 2*np.pi, N)
    #print(check)
    for c in check:
        x = x + s * np.cos(c)
        deltax = np.append(deltax, x)
        y = y + s * np.sin(c)
        deltay = np.append(deltay, y)
    return deltax, deltay

#probabilità di phi

def pf(phi):
    return 1/4*np.sin(0.5*phi)

#funzione cumulativa: c(x) = 1/2(1-cos(x/2))
def cf(phi):
    return 0.5 * (1-np.cos(0.5*phi))

def invcf(y):
    return 2 * np.arccos(1-2*y)

def random_walk2d_as(s, N):
    deltax = np.array([0])
    deltay = np.array([0])
    x = 0
    y = 0
    check = np.random.random(N)
    phi = invcf(check)
    #plt.figure(figsize=(18,9))

    #plt.hist(phi, bins = 100, range=(0, 2*np.pi), color = 'royalblue')
    #plt.xlabel('phi (rad)', fontsize = 20)
    #plt.ylabel('N')

    #plt.show()
    #print(check)
    for c in phi:
        x = x + s * np.cos(c)
        deltax = np.append(deltax, x)
        y = y + s * np.sin(c)
        deltay = np.append(deltay, y)
    return deltax, deltay


#simmetrica con sf

def random_walk2d_sf(s, sf, N):
    deltax = np.array([0])
    deltay = np.array([0])
    x = 0
    y = 0
    while(abs(x)<s*200):
    #    c = np.random.random()
    #    phi = invcf(c)
        check = np.random.uniform(0, 2*np.pi, N)
    #print(check)
    #for c in check:
        x = x + s * np.cos(check) + sf
        deltax = np.append(deltax, x)
        y = y + s * np.sin(check)
        deltay = np.append(deltay, y)
    return deltax, deltay


