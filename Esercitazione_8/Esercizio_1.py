import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy import constants, fft
from scipy import optimize

file_1 = pd.read_csv('data_sample1.csv')
file_2 = pd.read_csv('data_sample2.csv')
file_3 = pd.read_csv('data_sample3.csv')

f1t = file_1['time'].to_numpy()
f1m = file_1['meas'].to_numpy()

f2t = file_2['time'].to_numpy()
f2m = file_2['meas'].to_numpy()

f3t = file_3['time'].to_numpy()
f3m = file_3['meas'].to_numpy()

fig, ax = plt.subplots(1, 3, 
                    constrained_layout = True, figsize = (18, 6))

ax[0].plot(f1t, f1m, color='royalblue')
ax[1].plot(f2t, f2m, color='springgreen'  )
ax[2].plot(f3t, f3m,  color='sandybrown')

ax[0].set_title('Segnale 1', fontsize=15, color='royalblue')
ax[1].set_title('Segnale 2', fontsize=15, color='springgreen')
ax[2].set_title('Segnale 3', fontsize=15, color='sandybrown')

ax[0].set_xlabel('t (s)')
ax[0].set_ylabel('Ampiezza (u.a.)')

ax[1].set_xlabel('t (s)')
ax[1].set_ylabel('Ampiezza (u.a.)')

ax[2].set_xlabel('t (s)')
ax[2].set_ylabel('Ampiezza (u.a.)')

#for ax in fig.get_axes():
#    ax.label_outer()

plt.show()



fft1 = fft.rfft(f1m)
fftfreq1 = 0.5 * fft.rfftfreq(len(f1m), d = f1t[1]-f1t[0])
pot_1 = fft1.real ** 2 + fft1.imag ** 2

fft2 = fft.rfft(f2m)
fftfreq2 = 0.5 * fft.rfftfreq(len(f2m), d = f2t[1]-f2t[0])
pot_2 = fft2.real ** 2 + fft2.imag ** 2

fft3 = fft.rfft(f3m)
fftfreq3 = 0.5 * fft.rfftfreq(len(f3m), d = f3t[1]-f3t[0])
pot_3 = fft3.real ** 2 + fft3.imag ** 2


fig, ax = plt.subplots(1, 3, 
                    constrained_layout = True, figsize = (18, 6))

ax[0].plot(fftfreq1, pot_1, color='royalblue')
ax[1].plot(fftfreq2, pot_2, color='springgreen'  )
ax[2].plot(fftfreq3, pot_3,  color='sandybrown')

ax[0].set_title('Spettro di potenza segnale 1', fontsize=15, color='royalblue')
ax[1].set_title('Spettro di potenza segnale 2', fontsize=15, color='springgreen')
ax[2].set_title('Spettro di potenza segnale 3', fontsize=15, color='sandybrown')

ax[0].set_xlabel('f (Hz)')
ax[0].set_ylabel('Ampiezza (u.a.)')

ax[1].set_xlabel('f (Hz)')
ax[1].set_ylabel('Ampiezza (u.a.)')

ax[2].set_xlabel('f (Hz)')
ax[2].set_ylabel('Ampiezza (u.a.)')

#for ax in fig.get_axes():
#    ax.label_outer()

plt.show()


pot_1 = pot_1[fftfreq1!=0]
fftfreq1 = fftfreq1[fftfreq1!=0]
pot_2 = pot_2[fftfreq2!=0]
fftfreq2 = fftfreq2[fftfreq2!=0]
pot_3 = pot_3[5:]
fftfreq3 = fftfreq3[5:]

def fitfunc(x, a, n):
    return a / (x ** n) 

sigmaa = np.full(len(pot_1), 1)
#pstart = [177, 3, -10, 63, 0.03]

par_1, pcov_1 = optimize.curve_fit(fitfunc, xdata=fftfreq1, ydata=pot_1, 
                       sigma = sigmaa, absolute_sigma=True)

perr_1 = np.sqrt(np.diag(pcov_1))


plt.plot(fftfreq1, pot_1, color='royalblue')
plt.plot(fftfreq1, fitfunc(fftfreq1, par_1[0], par_1[1]), color='sandybrown')
plt.title('Fit potenza 1')
plt.xlabel('f (Hz)')
plt.ylabel('potenza (u.a.)')
plt.xscale('log')
plt.yscale('log')
plt.show()

pnames = ['a', 'n']

for pn, p, pe in zip(pnames, par_1,  perr_1):
    print('{:} = {:} +- {:}'.format( pn, p, pe))

sigmaa = np.full(len(pot_2), 1)

par_2, pcov_2 = optimize.curve_fit(fitfunc, xdata=fftfreq2, ydata=pot_2, 
                      sigma = sigmaa, absolute_sigma=True)

perr_2 = np.sqrt(np.diag(pcov_2))

plt.plot(fftfreq2, pot_2, color='springgreen')
plt.plot(fftfreq2, fitfunc(fftfreq2, par_2[0], par_2[1]), color='royalblue')
plt.title('Fit potenza 2')
plt.xlabel('f (Hz)')
plt.ylabel('potenza (u.a.)')
plt.xscale('log')
plt.yscale('log')
plt.show()

for pn, p, pe in zip(pnames, par_2,  perr_2):
    print('{:} = {:} +- {:}'.format( pn, p, pe))


sigmaa = np.full(len(pot_3), 1)

par_3, pcov_3 = optimize.curve_fit(fitfunc, xdata=fftfreq3, ydata=pot_3, 
                      sigma = sigmaa, absolute_sigma=True)

perr_3 = np.sqrt(np.diag(pcov_3))

plt.plot(fftfreq3, pot_3, color='sandybrown')
plt.plot(fftfreq3, fitfunc(fftfreq3, par_3[0], par_3[1]), color='springgreen')
#plt.plot(fftfreq3, fitfunc(fftfreq3, -1000, 2, 0), color='royalblue')
plt.title('Fit potenza 3')
plt.xlabel('f (Hz)')
plt.ylabel('potenza (u.a.)')
plt.xscale('log')
plt.yscale('log')
plt.show()


for pn, p, pe in zip(pnames, par_3,  perr_3):
    print('{:} = {:} +- {:}'.format( pn, p, pe))


#in ordine i rumori sono: bianco, rosa, rosso

