import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as color


file = pd.read_csv('oscilloscope.csv')


tempo = file['time']
segnale_1 = file['signal1']
segnale_2 = file['signal2']

plt.title('Segnale 1')
plt.plot(tempo, segnale_1, color='teal')
plt.xlabel('t')
plt.ylabel(r'V')
plt.show()



plt.title('Segnale 2')
plt.plot(tempo, segnale_2, color='springgreen')
plt.xlabel('t')
plt.ylabel(r'V')
plt.show()

plt.title('Segnali sovrapposti')
plt.plot(tempo, segnale_1, color='teal', label = 'Segnale 1')
plt.plot(tempo, segnale_2, color='springgreen', label = 'Segnale 2')
plt.xlabel('t')
plt.ylabel(r'V')
plt.legend()
plt.show()


def derivata(x, y):
    der = [(y[1]-y[0])/(x[1]-x[0])]
    for i in range(0, len(y)-2):
        der.append((y[i+2]-y[i])/(x[i+2]-x[i]))
    der.append((y[len(y)-1]-y[len(y)-2])/(x[len(y)-1]-x[len(y)-2]))
    return der


derivata_1 = derivata(tempo, segnale_1)

plt.plot(tempo, derivata_1, color='teal')
plt.title('Derivata segnale 1 con n = 2')
plt.xlabel('t')
plt.ylabel(r'dV/dt')
plt.show()



def derivata_n(x, y, n):
    indexmin = int(n/2)
    der = []
    for i in range(0, indexmin):
        der.append((y[n-i-1]-y[0])/(x[n-i-1]-x[0]))
    for i in range(0, len(y)-n):
        der.append((y[i+n]-y[i])/(x[i+n]-x[i]))
    for i in range(0, indexmin):
        der.append((y[len(y)-1]-y[len(y)-n-i])/(x[len(y)-1]-x[len(y)-n-1]))
    return der


derivata_corretta = derivata_n(tempo, segnale_1, 150)

plt.plot(tempo, derivata_corretta, color='teal')
plt.title('Derivata segnale 1 con n = 150')
plt.xlabel('t')
plt.ylabel(r'dV/dt')
plt.show()

