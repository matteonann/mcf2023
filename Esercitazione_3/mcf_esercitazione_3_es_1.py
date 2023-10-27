import pandas as pd
import matplotlib.pyplot as plt


file_dati = pd.read_csv('4FGL_J2202.7+4216_weekly_9_11_2023.csv')

print(file_dati)
print(file_dati.columns)

x = file_dati['Julian Date']
y = file_dati['Photon Flux [0.1-100 GeV](photons cm-2 s-1)']
erry = file_dati['Photon Flux Error(photons cm-2 s-1)']

#grafico normale 
plt.plot(x,y, 'o-', color = 'green')
plt.xlabel('Julian Date (d)')
plt.ylabel('Photon Flux [0.1-100 GeV](photons cm-2 s-1)')

plt.show()


#barre errore
plt.errorbar(x, y, yerr=erry, fmt='o' )

plt.xlabel('Julian Date (d)')
plt.ylabel('Photon Flux [0.1-100 GeV](photons cm-2 s-1)')
plt.savefig('figura_es_1.png')
plt.show()

#scala log

plt.errorbar(x, y, yerr=erry, fmt='o' )

plt.xlabel('Julian Date (d)')
plt.ylabel('Photon Flux [0.1-100 GeV](photons cm-2 s-1)')
plt.yscale('log')
plt.savefig('figura_es_1.png')
plt.show()



