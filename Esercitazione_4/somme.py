import numpy as np
import matplotlib.pyplot as plt

def somma(n):
    sum = 0
    for i in range(0,n+1):
        sum = sum+i
    return sum

def somma_radici(n):
    sum = 0
    for i in range(0,n+1):
        sum = sum+np.sqrt(i)
    return sum 

def somma_prodotto(n):
    sum = 0
    prod = 1
    for i in range(1, n+1):
        sum = sum+i
        prod = prod * i
    return sum, prod

def somma_potenza(n, alpha=1):
    sum = 0
    for i in range(0, n+1):
        sum = sum + i ** (alpha)
    return sum


    
