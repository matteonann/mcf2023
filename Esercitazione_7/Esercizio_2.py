import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt
import pandas as pd

#y = [theta, omega]

def f_ode_pendolo(y, t, lf):
    dydt = [y[1], -9.81/lf*np.sin(y[0])]
    return dydt

y0_1 = [45*np.pi/180, 0]
l_1 = 0.5

y0_2 = [45*np.pi/180, 0]
l_2 = 1

y0_3 = [30*np.pi/180, 0]
l_3 = 0.5


time = np.linspace(0, 10, 1001)

sol_1 = integrate.odeint(f_ode_pendolo, y0_1, time, args = (l_1, ))
sol_2 = integrate.odeint(f_ode_pendolo, y0_2, time, args = (l_2, ))
sol_3 = integrate.odeint(f_ode_pendolo, y0_3, time, args = (l_3, ))

fig,ax = plt.subplots(figsize=(9,6))
plt.plot(time, sol_1[:,0], label = '[theta0, l] = [45°, 0.5 m]')
plt.plot(time, sol_2[:,0], label = '[theta0, l] = [45°, 1 m]')
plt.plot(time, sol_3[:,0], label = '[theta0, l] = [30°, 0.5 m]')
plt.xlabel('t (s)')
plt.ylabel('theta (rad)')
plt.title('Soluzioni equazione pendolo semplice')
plt.ylim(-1.2, 1)
plt.legend(loc = 'lower left')
plt.show()

