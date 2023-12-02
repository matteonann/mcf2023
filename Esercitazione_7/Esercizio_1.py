import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy
from scipy import integrate

time = np.linspace(0, 10, 1001)


RC = np.array( [1, 0.1, 0.01] )


def V_in(t):
    Vin = np.ones(len(t))
    time_int = t.astype(int)
    time_odd = time_int % 2 != 0
    Vin[time_odd] = -1
    return Vin


#Con il metodo Runge-Kutta al 4o ordine

Vin_ar = V_in(time)

def f_ode_pb(V, t, Vinf, RCf):
    #1/RC(Vin-Vout)
        return 1/RCf * (Vinf - V)

# Dizionario 
soluzioniRK4 = {}

# Ciclo per diversi RC

for item in RC:
    h = time[1]-time[0]
    V0 = 0
    xx = np.empty((0,0))
    for t, vin in zip(time, Vin_ar):
        xx = np.append(xx, V0)
        k1 = h*f_ode_pb(V0,t, vin, item)
        k2 = h*f_ode_pb(V0+0.5*k1,t+0.5*h, vin, item)
        k3 = h*f_ode_pb(V0+0.5*k2,t+0.5*h, vin, item)
        k4 = h*f_ode_pb(V0+k3,t+h, vin, item)
        V0 += (k1+k2*2+k3*2+k4)/6 
    print(xx)
    soluzioniRK4.update({item : xx})
    fig,ax = plt.subplots(figsize=(9,6))
    plt.title('Soluzione equazione differenziale con RC = {:} Ohm F'.format(item), color='black', fontsize=14)
    plt.plot(time,Vin_ar, 'springgreen', label = 'Vin')
    plt.plot(time,xx, 'rebeccapurple', label = 'Vout')
    plt.xlabel('t (s)')
    plt.ylabel('Vout (V)')
    plt.legend()
    plt.show() 


fig, ax = plt.subplots(2, 2, 
                       constrained_layout = True, figsize = (18, 9))

ax[0, 0].plot(time, Vin_ar, color='lightsteelblue')
ax[0, 1].plot(time, soluzioniRK4[RC[0]] , color = 'dodgerblue')
ax[1, 0].plot(time, soluzioniRK4[RC[1]] , color = 'darkorchid')
ax[1, 1].plot(time, soluzioniRK4[RC[2]] , color = 'springgreen')


ax[0, 0].set_title('V in', fontsize=15, color='black')
ax[0, 1].set_title('V out con RC = 1', fontsize=15, color='dodgerblue')
ax[1, 0].set_title('V out con RC = 0.1', fontsize=15, color='darkorchid')
ax[1, 1].set_title('V out con RC = 0.01', fontsize=15, color='springgreen')

ax[0, 0].set_xlabel('t (s)')
ax[0, 0].set_ylabel('Vout (V)')

ax[0, 1].set_xlabel('t (s)')
ax[0, 1].set_ylabel('Vout (V)')

ax[1, 0].set_xlabel('t (s)')
ax[1, 0].set_ylabel('Vout (V)')

ax[1, 1].set_xlabel('t (s)')
ax[1, 1].set_ylabel('Vout (V)')

for ax in fig.get_axes():
    ax.label_outer()

plt.show()


#salvataggio

dataframe = pd.DataFrame( columns=['t', 'Vin', 'Vout RC = 1', 'Vout RC = 0.1', 'Vout RC = 0.01'])

dataframe['t'] = time
dataframe['Vin']   = Vin_ar
dataframe['Vout RC = 1']   = soluzioniRK4[RC[0]]
dataframe['Vout RC = 0.1']   = soluzioniRK4[RC[1]]
dataframe['Vout RC = 0.01']   = soluzioniRK4[RC[2]]

#dataframe.to_csv('passa_basso.csv', index=False)
