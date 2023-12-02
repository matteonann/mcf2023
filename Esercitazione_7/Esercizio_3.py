import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt
import pandas as pd

#y = [theta, omega]

def f_ode_osci(y, t, omegaf):
    dydt = [y[1], -omegaf**2*y[0]**3]
    return dydt

y0_1 = [0.5, 0]
omega_1 = 100

y0_2 = [0.1, 1]
omega_2 = 1000

y0_3 = [1, 0]
omega_3 = 500


time = np.linspace(0, 10, 1001)

sol_1 = integrate.odeint(f_ode_osci, y0_1, time, args = (omega_1, ))
sol_2 = integrate.odeint(f_ode_osci, y0_2, time, args = (omega_2, ))
sol_3 = integrate.odeint(f_ode_osci, y0_3, time, args = (omega_3, ))

fig,ax = plt.subplots(figsize=(9,6))
plt.plot(time, sol_1[:,0], 'red', alpha = 0.5, label = '[x0, v0, omega] = [{:} m, {:} m/s, {:} m^-1 s^-1]'.format(y0_1[0], y0_1[1], omega_1))
plt.plot(time, sol_2[:,0], 'blue', alpha = 0.5, label = '[x0, v0, omega] = [{:} m, {:} m/s, {:} m^-1 s^-1]'.format(y0_2[0], y0_2[1], omega_2))
plt.plot(time, sol_3[:,0], 'green', alpha = 0.5, label = '[x0, v0, omega] = [{:} m, {:} m/s, {:} m^-1 s^-1]'.format(y0_2[0], y0_2[1], omega_3))
plt.xlabel('t (s)')
plt.ylabel('x (m)')
plt.ylim(-1.6, 1.3)
plt.title('Soluzioni oscillatore anarmonico')
plt.legend(loc = 'lower left')
plt.show()
