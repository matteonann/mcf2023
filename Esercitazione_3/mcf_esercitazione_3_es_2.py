import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

file_dati = pd.read_csv('4LAC_DR2_sel.csv')
print(file_dati)
print(file_dati.columns)

print(file_dati.iloc[5:8])

y = file_dati['PL_Index']
x = file_dati['Flux1000']

plt.scatter(x, y, color = 'royalblue')
plt.xlabel("Flux1000")
plt.ylabel("PL_Index")

plt.show()

#asse x logaritmico

plt.scatter(x, y, color = 'royalblue')
plt.xlabel('Flux1000')
plt.ylabel('PL_Index')
plt.xscale('log')

plt.show()


#asse x log 10

file2 = file_dati.loc[( file_dati['nu_syn'] > 0)]

x1 = file2['nu_syn']
y1 = file2['PL_Index']
plt.scatter(x1, y1, color = 'royalblue')
plt.xlabel('nu_syn')
plt.ylabel('PL_Index')
plt.xscale('log')

plt.show()

file_bll = file2.loc[( file_dati['CLASS'] == 'bll')]
file_fsrq = file2.loc[( file_dati['CLASS'] == 'fsrq')]

#grafico sorgenti

xbll = file_bll['nu_syn']
xfsrq = file_fsrq['nu_syn']
ybll = file_bll['PL_Index']
yfsrq = file_fsrq['PL_Index']
plt.scatter(xbll, ybll, color = 'red', alpha = 0.5, label = 'bll')
plt.scatter(xfsrq, yfsrq, color = 'limegreen', alpha = 0.5, label = 'fsrq')
plt.xlabel('nu_syn')
plt.ylabel('PL_Index')
plt.xscale('log')
plt.legend()

plt.show()

#con errori

xbll = file_bll['nu_syn']
xfsrq = file_fsrq['nu_syn']
ybll = file_bll['PL_Index']
yfsrq = file_fsrq['PL_Index']
errbll = file_bll['Unc_PL_Index']
errfsrq = file_fsrq['Unc_PL_Index']
plt.errorbar(xbll, ybll, yerr = errbll, color = 'red', alpha = 0.5, label = 'bll')
plt.errorbar(xfsrq, yfsrq, yerr = errfsrq, color = 'limegreen', alpha = 0.5, label = 'fsrq')
plt.xlabel('nu_syn')
plt.ylabel('PL_Index')
plt.xscale('log')
plt.legend()

plt.show()

#istogrammi

nbill, binsbill, pbill = plt.hist(ybll, bins=50, range=(1, 3.5), color='royalblue', alpha=0.5, label = 'bll' )
nbill, binsbill, pbill = plt.hist(yfsrq, bins=50, range=(1, 3.5), color='limegreen', alpha=0.5, label = 'fsrq' )
plt.xlabel('PL_Index', fontsize=16)
plt.legend()
plt.show()

#ist log

nbill, binsbill, pbill = plt.hist(np.log10(ybll), bins=50, range=(0,0.8), color='royalblue', alpha=0.5, label = 'bll' )
nbill, binsbill, pbill = plt.hist(np.log10(yfsrq), bins=50, range=(0,0.8), color='limegreen', alpha=0.5, label = 'fsrq' )
plt.xlabel('PL_Index', fontsize=16)
plt.legend()
plt.show()


#grafici insieme

fig = plt.figure()
gs = fig.add_gridspec(2, 2, hspace=0, wspace=0)
(ax1, ax2), (ax3, ax4) = gs.subplots(sharex='col', sharey='row')
fig.suptitle('Sharing x per column, y per row')
ax3.scatter(np.log10(xbll), ybll, color = 'royalblue', alpha = 0.5, label = 'bll')
ax3.scatter(np.log10(xfsrq), yfsrq, color = 'limegreen', alpha = 0.5, label = 'fsrq')
ax2.set_visible(False)
#ax2.spines['top'].set_visible(False)
ax1.hist(np.log10(xbll), bins=50, range=(10,20), color='royalblue', alpha=0.5, label = 'bll' )
ax1.hist(np.log10(xfsrq), bins=50, range=(10,20), color='limegreen', alpha=0.5, label = 'fsrq' )
ax4.hist(ybll, bins=50, range=(1, 3.5), color='royalblue', alpha=0.5, label = 'bll', orientation='horizontal')
ax4.hist(yfsrq, bins=50, range=(1,3.5), color='limegreen', alpha=0.5, label = 'fsrq', orientation='horizontal')
ax1.set_ylabel('Number of sources')
ax3.set_ylabel('PL Index')
ax3.set_xlabel('log(nu_syn (Hz))')
ax4.set_xlabel('Number of sources')
for ax in fig.get_axes():
    ax.label_outer()
plt.show()
