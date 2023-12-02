from turtle import pd
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as color
import scipy
from scipy import optimize
from scipy import stats
#from scipy.optimize import curve_fit

dataset = pd.read_csv('Jpsimumu.csv')
#dataset = pd.read_csv('http://opendata.cern.ch/record/5203/files/Jpsimumu.csv')

en_1 = dataset['E1'].to_numpy()
en_2 = dataset['E2'].to_numpy()

px_1 = dataset['px1'].to_numpy()
px_2 = dataset['px2'].to_numpy()

py_1 = dataset['py1'].to_numpy()
py_2 = dataset['py2'].to_numpy()

pz_1 = dataset['pz1'].to_numpy()
pz_2 = dataset['pz2'].to_numpy()

m_inv = np.sqrt( (en_1 + en_2) ** 2 - ((px_1 + px_2) ** 2 + (py_1 + py_2) ** 2 + (pz_1 + pz_2) ** 2) ) 


fig,ax = plt.subplots(figsize=(10,7))

n, bins, p = plt.hist(m_inv, bins = 200, color = 'lightseagreen')
plt.title('Istogramma masse invarianti')
plt.xlabel('Masse invarianti (eV)')
plt.ylabel('Eventi')


ins = ax.inset_axes([0.6, 0.5, 0.32,0.37])
ins.hist(m_inv, bins = 200, range = (2.95, 3.25), color = 'rebeccapurple')
ins.set_title('Picco')

plt.show()


def fit_gauss(x, A, m, p1, p0, s):
  y = A*np.exp( -( x-m )**2/(2*s**2) ) + p1 * x + p0
  return y



def fit_gauss_2(x, A_1, m, s_1, A_2, s_2, p1, p0):
  y = A_1*np.exp( -( x-m )**2/(2*s_1**2) ) + A_2*np.exp( -( x-m )**2/(2*s_2**2) ) + p1 * x + p0
  return y

def retta(x, a, b):
   return a*x+b

def fit_gauss_3(x, A, m, s, p0):
  y = A*np.exp( -( x-m )**2/(2*s**2) ) + p0 * x
  return y

m_inv = np.sort(m_inv)
#mask_massa = np.logical_and(m_inv > 2.95, m_inv < 3.25)
mask_massa = [(x > 2.8) and (x < 3.4) for x in m_inv]

m_inv_rist = m_inv[mask_massa]

n_ristretto, bins_ristretto, p_ristretto = plt.hist(m_inv_rist, bins = 200, color = 'rebeccapurple')

bincenters = (bins_ristretto[:-1] + bins_ristretto[1:])/2


mask = np.nonzero(n_ristretto)

pstart = [177, 3, -10, 63, 0.03]
#pstart = [177, 3,  0.03]
par, pcov = optimize.curve_fit(fit_gauss, xdata=bincenters[mask], ydata=n_ristretto[mask], 
                      sigma=np.sqrt(n_ristretto[mask]), p0=pstart, absolute_sigma=True)

perr = np.sqrt(np.diag(pcov))



plt.plot(bincenters, fit_gauss(bincenters, par[0], par[1], par[2], par[3], par[4]), c='sandybrown')
plt.title('Istogramma masse invarianti')
plt.xlabel('Masse invarianti (eV)')
plt.ylabel('Eventi')
plt.show()

scarti = fit_gauss(bincenters, par[0], par[1], par[2], par[3], par[4]) - n_ristretto
sigma = np.sqrt(n_ristretto[mask])

scarti_sigma = scarti/sigma

plt.scatter(bincenters, scarti, c='sandybrown')
plt.title('Scarti')
plt.xlabel('Masse invarianti (eV)')
plt.ylabel('Scarti')
plt.show()




#Grafico con sotto scarti


fig, ax = plt.subplots(3,1, figsize=(9,6), gridspec_kw={'height_ratios': [3, 2, 2]}, sharex=True)
# Rimuovo spazio verticale fra i subplot
fig.subplots_adjust(hspace=0)

# Grafico subplot 0 (dati e funzione di fit)
ax[0].set_title('Fit Gaussiano', fontsize=16, color='rebeccapurple')
ax[0].hist(m_inv_rist, bins = 200, color = 'rebeccapurple')
ax[0].plot(bincenters, fit_gauss(bincenters, par[0], par[1], par[2], par[3], par[4]), c='sandybrown')
ax[0].set_ylabel('Eventi Misurati', fontsize=14)
ax[0].tick_params(axis="y", labelsize=14) 

# Grafico subplot 1 (rapporto dati / funzione di fit)
ax[1].errorbar(bincenters,  scarti, yerr = sigma, fmt='o', color='rebeccapurple' )
ax[1].set_xlabel('Massa invariante', fontsize =14)
ax[1].set_ylabel('Scarti',  fontsize =14)
ax[1].tick_params(axis="x",   labelsize=14) 
ax[1].tick_params(axis="y",   labelsize=14) 
ax[1].set_ylim(-60,60)       
ax[1].grid(True, axis='y')

ax[2].errorbar(bincenters,  abs(scarti_sigma), yerr = 1, fmt='o', color='rebeccapurple' )
ax[2].axhline(1, color='sandybrown') 
ax[2].set_xlabel('Massa invariante', fontsize =14)
ax[2].set_ylabel('|Scarti|/errore',  fontsize =14)
ax[2].tick_params(axis="x",   labelsize=14) 
ax[2].tick_params(axis="y",   labelsize=14) 
ax[2].set_ylim(-5,5)       
ax[2].grid(True, axis='y')
plt.show()

pnames = ['A', 'm', 's', 'p_1', 'p_0']

for pn, p, pe in zip(pnames, par,  perr):
    print('{:} = {:>6.4f} +- {:>6.4f}'.format( pn, p, pe))


# Calcolo Chi quadrato
# Valore funzine fit ottimizzata in corrispondneza dei tempi dei dati
yfit = fit_gauss(bincenters, par[0], par[1], par[2], par[3], par[4])

# chi2
chi2 =  np.sum( (yfit - n_ristretto)**2 /n_ristretto ) 

# gradi di libertà
ndof = len(n_ristretto)-len(par)

print('Chi2 / ndf: {:4.2f} / {:d} = {:2.3f}'.format( chi2, ndof, chi2/ndof ) )



plt.hist(m_inv_rist, bins = 200, color = 'rebeccapurple')


pstart_2 = [177, 3, 0.03, 100, 0.0003, -10, 63]
par_2, pcov_2 = optimize.curve_fit(fit_gauss_2, xdata=bincenters[mask], ydata=n_ristretto[mask], 
                      sigma=np.sqrt(n_ristretto[mask]), p0=pstart_2, absolute_sigma=True)

perr_2 = np.sqrt(np.diag(pcov_2))




plt.plot(bincenters, fit_gauss_2(bincenters, par_2[0], par_2[1], par_2[2], par_2[3], par_2[4], par_2[5], par_2[6]), c='sandybrown')
plt.title('Istogramma masse invarianti')
plt.xlabel('Masse invarianti (eV)')
plt.ylabel('Eventi')
plt.show()

pnames_2 = ['A_1', 'm', 's_1', 'A_2', 's_2', 'p_1', 'p_0']

for pn, p, pe in zip(pnames_2, par_2,  perr_2):
    print('{:} = {:>6.4f} +- {:>6.4f}'.format( pn, p, pe))




scarti_2 = fit_gauss_2(bincenters, par_2[0], par_2[1], par_2[2], par_2[3], par_2[4], par_2[5], par_2[6]) - n_ristretto
sigma = np.sqrt(n_ristretto[mask])

scarti2_sigma = scarti_2/sigma

plt.scatter(bincenters, scarti_2, c='sandybrown')
plt.title('Scarti')
plt.xlabel('Masse invarianti (eV)')
plt.ylabel('Scarti')
plt.show()

fig, ax = plt.subplots(3,1, figsize=(9,6), gridspec_kw={'height_ratios': [3, 2, 2]}, sharex=True)
# Rimuovo spazio verticale fra i subplot
fig.subplots_adjust(hspace=0)

# Grafico subplot 0 (dati e funzione di fit)
ax[0].set_title('Fit Gaussiano 2', fontsize=16, color='rebeccapurple')
ax[0].hist(m_inv_rist, bins = 200, color = 'rebeccapurple')
ax[0].plot(bincenters, fit_gauss_2(bincenters, par_2[0], par_2[1], par_2[2], par_2[3], par_2[4], par_2[5], par_2[6]), c='sandybrown')
ax[0].set_ylabel('Eventi Misurati', fontsize=14)
ax[0].tick_params(axis="y", labelsize=14) 

# Grafico subplot 1 (rapporto dati / funzione di fit)
ax[1].errorbar(bincenters,  scarti_2, yerr = sigma, fmt='o', color='rebeccapurple' )
ax[1].set_xlabel('Massa invariante', fontsize =14)
ax[1].set_ylabel('Scarti',  fontsize =14)
ax[1].tick_params(axis="x",   labelsize=14) 
ax[1].tick_params(axis="y",   labelsize=14) 
ax[1].set_ylim(-50,50)       
ax[1].grid(True, axis='y')

ax[2].errorbar(bincenters,  abs(scarti2_sigma), yerr = 1, fmt='o', color='rebeccapurple' )
ax[2].axhline(1, color='sandybrown') 
ax[2].set_xlabel('Massa invariante', fontsize =14)
ax[2].set_ylabel('|Scarti|/errore',  fontsize =14)
ax[2].tick_params(axis="x",   labelsize=14) 
ax[2].tick_params(axis="y",   labelsize=14) 
ax[2].set_ylim(-5,5)       
ax[2].grid(True, axis='y')
plt.show()


yfit2 = fit_gauss_2(bincenters, par_2[0], par_2[1], par_2[2], par_2[3], par_2[4], par_2[5], par_2[6])

# chi2
chi22 =  np.sum( (yfit2 - n_ristretto)**2 /n_ristretto ) 

# gradi di libertà
ndof2 = len(n_ristretto)-len(par_2)

print('Chi2 / ndf: {:4.2f} / {:d} = {:2.3f}'.format( chi22, ndof2, chi22/ndof2 ) )



#secondo picco


mask_massa3 = [(x > 3.4) and (x < 4) for x in m_inv]

m_inv_rist3 = m_inv[mask_massa3]

n_ristretto3, bins_ristretto3, p_ristretto3 = plt.hist(m_inv_rist3, bins = 200, color = 'rebeccapurple')

bincenters3 = (bins_ristretto3[:-1] + bins_ristretto3[1:])/2


mask3 = np.nonzero(n_ristretto3)

pstart3 = [177, 3, 0.03, 100, 0.0003, -10, 63]
par3, pcov3 = optimize.curve_fit(fit_gauss_2, xdata=bincenters3[mask3], ydata=n_ristretto3[mask3], 
                      sigma=np.sqrt(n_ristretto3[mask3]), absolute_sigma=True)

perr3 = np.sqrt(np.diag(pcov))



plt.plot(bincenters3, fit_gauss_2(bincenters3, par3[0], par3[1], par3[2], par3[3], par3[4], par3[5], par3[6]), c='sandybrown')
plt.title('Istogramma masse invarianti')
plt.xlabel('Masse invarianti (eV)')
plt.ylabel('Eventi')
plt.show()

scarti3 = fit_gauss_2(bincenters3, par3[0], par3[1], par3[2], par3[3], par3[4], par3[5], par3[6]) - n_ristretto3
sigma3 = np.sqrt(n_ristretto3[mask3])

scarti_sigma3 = scarti3/sigma3

plt.scatter(bincenters3, scarti3, c='sandybrown')
plt.title('Scarti')
plt.xlabel('Masse invarianti (eV)')
plt.ylabel('Scarti')
plt.show()




#Grafico con sotto scarti


# Grafico con due subplot
fig, ax = plt.subplots(3,1, figsize=(9,6), gridspec_kw={'height_ratios': [3, 2, 2]}, sharex=True)
# Rimuovo spazio verticale fra i subplot
fig.subplots_adjust(hspace=0)

# Grafico subplot 0 (dati e funzione di fit)
ax[0].set_title('Fit Gaussiano 2 picco secondario', fontsize=16, color='rebeccapurple')
ax[0].hist(m_inv_rist3, bins = 200, color = 'rebeccapurple')
ax[0].plot(bincenters3, fit_gauss_2(bincenters3, par3[0], par3[1], par3[2], par3[3], par3[4], par3[5], par3[6]), c='sandybrown')
ax[0].set_ylabel('Eventi Misurati', fontsize=14)
ax[0].tick_params(axis="y", labelsize=14) 

# Grafico subplot 1 (rapporto dati / funzione di fit)
ax[1].errorbar(bincenters3,  scarti3, yerr = sigma3, fmt='o', color='rebeccapurple' )
ax[1].set_xlabel('Massa invariante', fontsize =14)
ax[1].set_ylabel('Scarti',  fontsize =14)
ax[1].tick_params(axis="x",   labelsize=14) 
ax[1].tick_params(axis="y",   labelsize=14) 
ax[1].set_ylim(-60,60)       
ax[1].grid(True, axis='y')

ax[2].errorbar(bincenters3,  abs(scarti_sigma3), yerr = 1, fmt='o', color='rebeccapurple' )
ax[2].axhline(1, color='sandybrown') 
ax[2].set_xlabel('Massa invariante', fontsize =14)
ax[2].set_ylabel('|Scarti|/errore',  fontsize =14)
ax[2].tick_params(axis="x",   labelsize=14) 
ax[2].tick_params(axis="y",   labelsize=14) 
ax[2].set_ylim(-5,5)       
ax[2].grid(True, axis='y')
plt.show()

pnames3 = ['A_1', 'm', 's_1', 'A_2', 's_2', 'p_1', 'p_0']

for pn, p, pe in zip(pnames3, par3,  perr3):
    print('{:} = {:>6.4f} +- {:>6.4f}'.format( pn, p, pe))


yfit3 = fit_gauss_2(bincenters3, par3[0], par3[1], par3[2], par3[3], par3[4], par3[5], par3[6])

# chi2
chi23 =  np.sum( (yfit3 - n_ristretto3)**2 /n_ristretto3 ) 

# gradi di libertà
ndof3 = len(n_ristretto3)-len(par3)

print('Chi2 / ndf: {:4.2f} / {:d} = {:2.3f}'.format( chi23, ndof3, chi23/ndof3 ) )

