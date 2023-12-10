import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy import constants, fft
from scipy import optimize
import matplotlib.colors as color


file = pd.read_csv('copernicus_PG_selected.csv')

t_old = file['date_old'].to_numpy()
t = file['date'].to_numpy()
c_co=file['mean_co_ug/m3'].to_numpy()
c_nh3=file['mean_nh3_ug/m3'].to_numpy()
c_no2=file['mean_no2_ug/m3'].to_numpy()
c_o3=file['mean_o3_ug/m3'].to_numpy()
c_pm10=file['mean_pm10_ug/m3'].to_numpy()
c_pm2p5=file['mean_pm2p5_ug/m3'].to_numpy()
c_so2=file['mean_so2_ug/m3'].to_numpy()

plt.figure(figsize = (18,9))
plt.plot(t, c_co, label = 'CO', color = 'indianred')
plt.plot(t, c_nh3, label = 'NH3', color = 'goldenrod')
plt.plot(t, c_no2, label = 'NO2', color = 'mediumseagreen')
plt.plot(t, c_o3, label = 'O3', color = 'teal')
plt.plot(t, c_pm10, label = 'Pm10', color = 'steelblue')
plt.plot(t, c_pm2p5, label = 'Pm2P5', color = 'darkslateblue')
plt.plot(t, c_so2, label = 'SO2', color = 'darkorchid')
plt.ylabel('Concentrazione (ug/m^3)')
plt.xlabel('t (giorni)')
plt.title('Concentrazioni degli agenti inquinanti')
plt.legend()
plt.show()


#plt.figure(figsize = (18,9))
#plt.plot(t_old, c_co, label = 'CO', color = 'indianred')
#plt.plot(t_old, c_nh3, label = 'NH3', color = 'goldenrod')
#plt.plot(t_old, c_no2, label = 'NO2', color = 'mediumseagreen')
#plt.plot(t_old, c_o3, label = 'O3', color = 'teal')
#plt.plot(t_old, c_pm10, label = 'Pm10', color = 'steelblue')
#plt.plot(t_old, c_pm2p5, label = 'Pm2P5', color = 'darkslateblue')
#plt.plot(t_old, c_so2, label = 'SO2', color = 'darkorchid')
#plt.ylabel('Concentrazione (ug/m^3)')
#plt.xlabel('t (u.a.)')
#plt.title('Concentrazioni degli agenti inquinanti')
#plt.legend()
#plt.show()

fft_co = fft.rfft(c_co)
fftfreq_co =  fft.rfftfreq(len(c_co), d = 1)
print(len(fft_co), len(fftfreq_co))
pot_co = fft_co.real ** 2 + fft_co.imag ** 2

fft_nh3 = fft.rfft(c_nh3)
fftfreq_nh3 = 0.5 * fft.rfftfreq(len(c_nh3), d = t[1]-t[0])
pot_nh3 = fft_nh3.real ** 2 + fft_nh3.imag ** 2

fft_no2 = fft.rfft(c_no2)
fftfreq_no2 = 0.5 * fft.rfftfreq(len(c_no2), d = t[1]-t[0])
pot_no2 = fft_no2.real ** 2 + fft_no2.imag ** 2

fft_o3 = fft.rfft(c_o3)
fftfreq_o3 = 0.5 * fft.rfftfreq(len(c_o3), d = t[1]-t[0])
pot_o3 = fft_o3.real ** 2 + fft_o3.imag ** 2

fft_pm10 = fft.rfft(c_pm10)
fftfreq_pm10 = 0.5 * fft.rfftfreq(len(c_pm10), d = t[1]-t[0])
pot_pm10 = fft_pm10.real ** 2 + fft_pm10.imag ** 2

fft_pm2p5 = fft.rfft(c_pm2p5)
fftfreq_pm2p5 = 0.5 * fft.rfftfreq(len(c_pm2p5), d = t[1]-t[0])
pot_pm2p5 = fft_pm2p5.real ** 2 + fft_pm2p5.imag ** 2

fft_no2 = fft.rfft(c_no2)
fftfreq_no2 = 0.5 * fft.rfftfreq(len(c_no2), d = t[1]-t[0])
pot_no2 = fft_no2.real ** 2 + fft_no2.imag ** 2

plt.figure(figsize = (18,9))
plt.plot(fftfreq_co, pot_co, label = 'CO', color = 'indianred')
#plt.plot(fftfreq_nh3, pot_nh3, label = 'NH3', color = 'goldenrod')
#plt.plot(fftfreq_no2, pot_no2, label = 'NO2', color = 'mediumseagreen')
#plt.plot(fftfreq_o3, pot_o3, label = 'O3', color = 'teal')
#plt.plot(fftfreq_pm10, pot_pm10, label = 'Pm10', color = 'steelblue')
#plt.plot(fftfreq_pm2p5, pot_pm2p5, label = 'Pm2P5', color = 'darkslateblue')
#plt.plot(fftfreq_no2, pot_no2, label = 'SO2', color = 'darkorchid')
plt.ylabel('Potenza (u.a.)')
plt.xlabel('f (1/giorni)')
plt.yscale('log')
plt.xscale('log')
plt.title('Spettro di potenza')
plt.show()

plt.figure(figsize = (18,9))
plt.plot(1/fftfreq_co[1:], pot_co[1:], label = 'CO', color = 'indianred')
#plt.plot(1/fftfreq_nh3[1:], pot_nh3[1:], label = 'NH3', color = 'goldenrod')
#plt.plot(1/fftfreq_no2[1:], pot_no2[1:], label = 'NO2', color = 'mediumseagreen')
#plt.plot(1/fftfreq_o3[1:], pot_o3[1:], label = 'O3', color = 'teal')
#plt.plot(1/fftfreq_pm10[1:], pot_pm10[1:], label = 'Pm10', color = 'steelblue')
#plt.plot(1/fftfreq_pm2p5[1:], pot_pm2p5[1:], label = 'Pm2P5', color = 'darkslateblue')
#plt.plot(1/fftfreq_no2[1:], pot_no2[1:], label = 'SO2', color = 'darkorchid')
plt.ylabel('Potenza (u.a.)')
plt.xlabel('T (giorni)')
plt.yscale('log')
plt.xscale('log')
plt.title('Spettro di potenza')
plt.show()

#mask = [(item > 0.0008) and (item <0.0066) for item in fftfreq_co]
mask = pot_co > 5e06
#periodicità di circa 1 anno


plt.figure(figsize = (18,9))
plt.plot(fftfreq_co[mask], pot_co[mask], label = 'CO', color = 'indianred')
#plt.plot(fftfreq_nh3, pot_nh3, label = 'NH3', color = 'goldenrod')
#plt.plot(fftfreq_no2, pot_no2, label = 'NO2', color = 'mediumseagreen')
#plt.plot(fftfreq_o3, pot_o3, label = 'O3', color = 'teal')
#plt.plot(fftfreq_pm10, pot_pm10, label = 'Pm10', color = 'steelblue')
#plt.plot(fftfreq_pm2p5, pot_pm2p5, label = 'Pm2P5', color = 'darkslateblue')
#plt.plot(fftfreq_no2, pot_no2, label = 'SO2', color = 'darkorchid')
plt.ylabel('Potenza (u.a.)')
plt.xlabel('f (1/giorni)')
plt.yscale('log')
plt.xscale('log')
plt.title('Spettrio di potenza')
plt.show()


c_co_filtrata = fft.irfft(fft_co[mask], n=len(t))


plt.figure(figsize = (18,9))
plt.plot(t, c_co_filtrata,  label = 'concentrazione CO filtrata', color = 'darkslateblue', linewidth=2.0)
plt.plot(t, c_co, label = 'concentrazione CO non filtrata', color = 'indianred')
plt.ylabel('Concentrazione (ug/m^3)')
plt.xlabel('t (giorni)')
plt.title('Concentrazione di CO')
plt.legend()
plt.show()