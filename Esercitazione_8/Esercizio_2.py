import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy import constants, fft
from scipy import optimize
import matplotlib.colors as color

df_1 = pd.read_csv('4FGL_J2202.7+4216_weekly_9_15_2023_mcf.csv')
df_2 = pd.read_csv('4FGL_J0721.9+7120_weekly_9_15_2023_mcf.csv')
df_3 = pd.read_csv('4FGL_J0428.6-3756_weekly_9_15_2023_mcf.csv')
df_4 = pd.read_csv('4FGL_J1256.1-0547_weekly_9_15_2023_mcf.csv')
df_5 = pd.read_csv('4FGL_J2253.9+1609_weekly_9_15_2023_mcf.csv')
df_6 = pd.read_csv('4FGL_J2232.6+1143_weekly_9_15_2023_mcf.csv')

flux1 = df_1['Photon Flux [0.1-100 GeV](photons cm-2 s-1)'].to_numpy()
flux2 = df_2['Photon Flux [0.1-100 GeV](photons cm-2 s-1)'].to_numpy()
flux3 = df_3['Photon Flux [0.1-100 GeV](photons cm-2 s-1)'].to_numpy()
flux4 = df_4['Photon Flux [0.1-100 GeV](photons cm-2 s-1)'].to_numpy()
flux5 = df_5['Photon Flux [0.1-100 GeV](photons cm-2 s-1)'].to_numpy()
flux6 = df_6['Photon Flux [0.1-100 GeV](photons cm-2 s-1)'].to_numpy()


jd1 = df_1['Julian Date'].to_numpy()
jd2 = df_2['Julian Date'].to_numpy()
jd3 = df_3['Julian Date'].to_numpy()
jd4 = df_4['Julian Date'].to_numpy()
jd5 = df_5['Julian Date'].to_numpy()
jd6 = df_6['Julian Date'].to_numpy()




plt.figure(figsize = (18,9))
plt.plot(jd1, flux1, label = 'sorgente Bl Lac , classe BLL', color = 'indianred')
plt.plot(jd2, flux2, label = 'sorgente S5 0716+71 , classe BLL', color = 'goldenrod')
plt.plot(jd3, flux3, label = 'sorgente PKS 0426-380 , classe BLL', color = 'mediumseagreen')
plt.plot(jd4, flux4, label = 'sorgente 3C 279 , classe FSRQ', color = 'teal')
plt.plot(jd5, flux5, label = 'sorgente 3C 454.3 , classe FSRQ', color = 'steelblue')
plt.plot(jd6, flux6, label = 'sorgente CTA 102 , classe FSRQ', color = 'rebeccapurple')
plt.ylabel('Photon Flux')
plt.xlabel('Julian Date')
plt.title('Curve di luce')
plt.legend()
plt.show()



fig, ax = plt.subplots(3,2, figsize=(18,9), gridspec_kw={'height_ratios': [1, 1, 1]}, sharex=True)
fig.subplots_adjust(hspace=0.3)


ax[0,0].set_title('sorgente Bl Lac , classe BLL', fontsize=16, color='steelblue')
ax[0,0].plot(jd1, flux1, color = 'steelblue')
ax[0,0].set_xlabel('Photon Flux', fontsize = 14)
ax[0,0].set_ylabel('Photon Flux', fontsize = 14)

# Grafico subplot 1 (rapporto dati / funzione di fit)
ax[0,1].set_title('sorgente 3C 279 , classe FSRQ', fontsize=16, color='crimson')
ax[0,1].plot(jd2, flux2, color = 'crimson')
ax[0,1].set_xlabel('Photon Flux', fontsize = 14)
ax[0,1].set_ylabel('Photon Flux', fontsize = 14)

ax[1,0].set_title('sorgente S5 0716+71 , classe BLL', fontsize=16, color='steelblue')
ax[1,0].plot(jd3, flux3, color = 'steelblue')
ax[1,0].set_xlabel('Photon Flux', fontsize = 14)
ax[1,0].set_ylabel('Photon Flux', fontsize = 14)

ax[1,1].set_title('sorgente 3C 454.3 , classe FSRQ', fontsize=16, color='crimson')
ax[1,1].plot(jd4, flux4, color = 'crimson')
ax[1,1].set_xlabel('Photon Flux', fontsize = 14)
ax[1,1].set_ylabel('Photon Flux', fontsize = 14)

# Grafico subplot 1 (rapporto dati / funzione di fit)
ax[2,0].set_title('sorgente PKS 0426-380 , classe BLL', fontsize=16, color='steelblue')
ax[2,0].plot(jd5, flux5, color = 'steelblue')
ax[2,0].set_xlabel('Photon Flux', fontsize = 14)
ax[2,0].set_ylabel('Photon Flux', fontsize = 14)

ax[2,1].set_title('sorgente CTA 102 , classe FSRQ', fontsize=16, color='crimson')
ax[2,1].plot(jd6, flux6, color = 'crimson')
ax[2,1].set_xlabel('Photon Flux', fontsize = 14)
ax[2,1].set_ylabel('Photon Flux', fontsize = 14)
plt.show()


fft1 = fft.rfft(flux1)
fftfreq1 = 0.5 * fft.rfftfreq(len(flux1), d = jd1[1]-jd1[0])
pot_1 = fft1.real ** 2 + fft1.imag ** 2

fft2 = fft.rfft(flux2)
fftfreq2 = 0.5 * fft.rfftfreq(len(flux2), d = jd2[1]-jd2[0])
pot_2 = fft2.real ** 2 + fft2.imag ** 2

fft3 = fft.rfft(flux3)
fftfreq3 = 0.5 * fft.rfftfreq(len(flux3), d = jd3[1]-jd3[0])
pot_3 = fft3.real ** 2 + fft3.imag ** 2

fft4 = fft.rfft(flux4)
fftfreq4 = 0.5 * fft.rfftfreq(len(flux4), d = jd4[1]-jd4[0])
pot_4 = fft4.real ** 2 + fft4.imag ** 2

fft5 = fft.rfft(flux5)
fftfreq5 = 0.5 * fft.rfftfreq(len(flux5), d = jd5[1]-jd5[0])
pot_5 = fft5.real ** 2 + fft5.imag ** 2

fft6 = fft.rfft(flux6)
fftfreq6 = 0.5 * fft.rfftfreq(len(flux6), d = jd6[1]-jd6[0])
pot_6 = fft6.real ** 2 + fft6.imag ** 2


plt.figure(figsize = (18,9))
plt.plot(fftfreq1, pot_1, label = 'sorgente Bl Lac , classe BLL', color = 'indianred')
plt.plot(fftfreq2, pot_2, label = 'sorgente S5 0716+71 , classe BLL', color = 'goldenrod')
plt.plot(fftfreq3, pot_3, label = 'sorgente PKS 0426-380 , classe BLL', color = 'mediumseagreen')
plt.plot(fftfreq4, pot_4, label = 'sorgente 3C 279 , classe FSRQ', color = 'teal')
plt.plot(fftfreq5, pot_5, label = 'sorgente 3C 454.3 , classe FSRQ', color = 'steelblue')
plt.plot(fftfreq6, pot_6, label = 'sorgente CTA 102 , classe FSRQ', color = 'rebeccapurple')
plt.ylabel('Potenza (u.a.)')
plt.xlabel('f (u.a.)')
plt.yscale('log')
plt.xscale('log')
plt.title('Spettri di potenza')
plt.show()



plt.figure(figsize = (18,9))
plt.plot(fftfreq1, pot_1, label = 'classe BLL', color = 'steelblue')
plt.plot(fftfreq2, pot_2, label = 'classe BLL', color = 'steelblue')
plt.plot(fftfreq3, pot_3, label = 'classe BLL', color = 'steelblue')
plt.plot(fftfreq4, pot_4, label = 'classe FSRQ', color = 'crimson')
plt.plot(fftfreq5, pot_5, label = 'classe FSRQ', color = 'crimson')
plt.plot(fftfreq6, pot_6, label = 'classe FSRQ', color = 'crimson')
plt.ylabel('Potenza (u.a.)')
plt.xlabel('f (u.a.)')
plt.yscale('log')
plt.xscale('log')
plt.title('Spettri di potenza')
plt.show()


pot_1_norm = pot_1/pot_1[0]
pot_2_norm = pot_2/pot_2[0]
pot_3_norm = pot_3/pot_3[0]
pot_4_norm = pot_4/pot_4[0]
pot_5_norm = pot_5/pot_5[0]
pot_6_norm = pot_6/pot_6[0]
print(pot_1_norm[0], pot_2_norm[0], pot_3_norm[0], pot_4_norm[0], pot_5_norm[0], pot_6_norm[0])

plt.figure(figsize = (18,9))
plt.plot(fftfreq1, pot_1_norm, label = 'classe BLL', color = 'steelblue')
plt.plot(fftfreq2, pot_2_norm, label = 'classe BLL', color = 'steelblue')
plt.plot(fftfreq3, pot_3_norm, label = 'classe BLL', color = 'steelblue')
plt.plot(fftfreq4, pot_4_norm, label = 'classe FSRQ', color = 'crimson')
plt.plot(fftfreq5, pot_5_norm, label = 'classe FSRQ', color = 'crimson')
plt.plot(fftfreq6, pot_6_norm, label = 'classe FSRQ', color = 'crimson')
plt.ylabel('Potenza (u.a.)')
plt.xlabel('f (u.a.)')
plt.title('Spettri di potenza normalizzati')
plt.show()


plt.figure(figsize = (18,9))
plt.plot(fftfreq1, pot_1_norm, label = 'classe BLL', color = 'steelblue')
plt.plot(fftfreq2, pot_2_norm, label = 'classe BLL', color = 'steelblue')
plt.plot(fftfreq3, pot_3_norm, label = 'classe BLL', color = 'steelblue')
plt.plot(fftfreq4, pot_4_norm, label = 'classe FSRQ', color = 'crimson')
plt.plot(fftfreq5, pot_5_norm, label = 'classe FSRQ', color = 'crimson')
plt.plot(fftfreq6, pot_6_norm, label = 'classe FSRQ', color = 'crimson')
plt.ylabel('Potenza (u.a.)')
plt.xlabel('f (u.a.)')
plt.yscale('log')
plt.xscale('log')
plt.title('Spettri di potenza normalizzati scala log')
plt.show()