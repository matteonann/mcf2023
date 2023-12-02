import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.colors as color
from scipy import integrate
import argparse
import sys,os

xx = np.arange(-5,5.05, 0.1)



def parse_arguments():
    
    parser = argparse.ArgumentParser(description='Argparse per scelta dei potenziali.',
                                     usage      ='python3 Esercizio_2.py  --opzione')
    parser.add_argument('-6', '--opzione1',    action='store_true',                          help='Potenziale x^6')
    parser.add_argument('-2', '--opzione2',    action='store_true',
            help='Potenziale x^2?')
    parser.add_argument('-4', '--opzione3',    action='store_true',
            help='Potenziale x^4?')
    parser.add_argument('-32', '--opzione4',    action='store_true',
            help='Potenziale x^3/2?')
    return  parser.parse_args()


xx = np.arange(-5,5.05, 0.1)
distanze = xx[xx>=0]

    

def V(x, k, esp):
    return k * x ** esp

def periodi(dist, esp, k, m):
    periodi = []
    for i in range(1, len(dist)):
        x_0 = dist[i]
        interv = np.arange(0, x_0 * 10000, 0.1)/10000
        V_0 = V(x_0, k, esp)
        integranda = 4*np.sqrt(8*m)*1/np.sqrt(V_0-V(interv, k, esp))
        integ = integrate.simpson(integranda, dx = 0.1/10000)
        periodi.append(integ)
    return periodi


def grafico(x, esp, k, titolo):
    plt.plot(x, V(x, k, esp), color='teal')
    plt.axvline(color='k', linewidth=0.5)
    plt.title('{:}'.format(titolo))
    plt.xlabel('x')
    plt.ylabel(r'V(x)')
    plt.plot(4.5, V(4.5,k, esp) , 'o', markersize=12, color='indianred')
    plt.show()


k = 100
esp_2 = 2
esp_6 = 6
esp_4 = 4
esp_32 = 3/2
m = 0.5

def grafici():

    args = parse_arguments()

    
    
    if args.opzione1 == True:

        grafico(xx, esp_6, k, 'Potenziale V(x)=x^6')


        
    if args.opzione2 == True:

        grafico(xx, esp_2, k, 'Potenziale V(x)=x^2')

        
    if args.opzione3 == True:

        grafico(xx, esp_4, k, 'Potenziale V(x)=x^4')
 

    if args.opzione4 == True:

        grafico(distanze, esp_32, k, 'Potenziale V(x)=|x|^3/2')


#Inserisco i grafici dei periodi in altre istruzioni condizionali per rappresentare tutti quelli richiesti in un grafico unico dopo aver rappresentato uno alla volta i potenziali

    if args.opzione1 == True:


        per_6 = periodi(distanze, esp_6, k, m)
        plt.plot(distanze[1:], per_6, color='teal', label = 'x^6')
 

        
    if args.opzione2 == True:


        per_2 = periodi(distanze, esp_2, k, m)
        plt.plot(distanze[1:], per_2, color='indianred', label = 'x^2')


        
    if args.opzione3 == True:


        per_4 = periodi(distanze, esp_4, k, m)
        plt.plot(distanze[1:], per_4, color='royalblue', label = 'x^4')
 


    if args.opzione4 == True:

 
        per_32 = periodi(distanze, esp_32, k, m)
        plt.plot(distanze[1:], per_32, color='springgreen', label = '|x|^3/2')

        
    plt.xlabel('x0 (m)')
    plt.ylabel('T (s)')
    plt.legend()
    plt.show()
        

        
if __name__ == "__main__":

    grafici()
