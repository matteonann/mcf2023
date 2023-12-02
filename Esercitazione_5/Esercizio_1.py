import numpy as np
import matplotlib.pyplot as plt
from  scipy import integrate
import matplotlib.colors as colors
import math
import pandas as pd
import argparse
import sys,os

file = pd.read_csv('vel_vs_time.csv')

tempi = file['t']
velocita = file['v']


#plt.plot(tempi, velocita, color = 'rebeccapurple')
#plt.xlabel('t (s)')
#plt.ylabel('v (m/s)')
#plt.show()



#distanza  = integrate.simpson(  velocita, x = tempi,  dx=5)

#distanze = []
#for i in range(1, len(velocita)+1):
#    distanze.append(integrate.simpson(velocita[:i], x = tempi[:i], dx = 0.5))

#plt.plot(tempi, distanze, color = 'rebeccapurple')
#plt.xlabel('t (s)')
#plt.ylabel('x (m)')
#plt.show()



def parse_arguments():
    
    parser = argparse.ArgumentParser(description='Argparse per visualizzazione grafici',
                                     usage      ='python3 Esercizio_1.py  --opzione')
    parser.add_argument('-v', '--opzione1',    action='store_true',                          help='Vuoi la v?')
    parser.add_argument('-x', '--opzione2',    action='store_true',
            help='Vuoi la x?')
    return  parser.parse_args()


def grafici():

    args = parse_arguments()

    # print 
    #print(args)

    #if args.opzione1 == True:
    #    print('---------------------------------------------')
    #    print('   Opzione 1 = True')
    #    print('---------------------------------------------')

    
    
    if args.opzione1 == True:

        plt.plot(tempi, velocita, color = 'rebeccapurple')
        plt.xlabel('t (s)')
        plt.ylabel('v (m/s)')
        plt.show()

    if args.opzione2 == True:


        distanze = []
        for i in range(1, len(velocita)+1):
            distanze.append(integrate.simpson(velocita[:i], x = tempi[:i], dx = 0.5))

        plt.plot(tempi, distanze, color = 'rebeccapurple')
        plt.xlabel('t (s)')
        plt.ylabel('x (m)')
        plt.show()


if __name__ == "__main__":

    grafici()
