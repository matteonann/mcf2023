import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as color
import pandas as pd
from tqdm import tqdm



# modulo time necessario per utilizzare sleep


def random_walk2d_sf(su, sf):
    c = np.random.uniform(0, 2*np.pi)
    x = su * np.cos(c) 
    y = su * np.sin(c) + sf
    return x, y




class camera:
    def __init__(self, a, b):
        self.thickness = a     
        self.n_p = b
    def sim_part(self):
        ncouples = np.random.poisson(lam = self.n_p)
        position = np.random.uniform(-(self.thickness)/2, (self.thickness)/2, ncouples)
        return ncouples, position
    
    def sim_diff(self, su, sf, nr, pos, tc):
        
        #s_x = np.array([0])
        #s_y = np.array([0])
        nsteps = 0
        x = 0
        y = pos
        if (pos > 0):
            sf = - sf
        rivelato = 1
        while(abs(y) > 0.01):
            xsf, ysf = random_walk2d_sf(su, sf)
            x = x + xsf
            y = y + ysf
            #s_x.append(x)
            #s_y.append(y)
            nsteps = nsteps + 1
            p_ass = np.random.binomial(1, 1/nr)
            if (p_ass == 1):
                rivelato = 0
                break
        td = tc * nsteps
        return td, rivelato
        

class evento:
    def __init__(self, a, b, c, d):
        self.n_gen = a     
        self.n_riv = b
        self.td_riv = c
        self.pos0_riv = d


N_part = input('Quante particelle vuoi simulare? ')
N_part = int(N_part)
N_p = 5
S_u = 1e-04
S_f = 5e-05
N_r = 1e04
T_c = 1e-12




mwpc = camera(1, N_p)
arr_eventi = []


for part in tqdm(range(0, N_part)):
    
    n_c, pos = mwpc.sim_part()
    tempi = []
    rivelazioni = 0
    for i in range(0, n_c):
        tempo, rivelazione = mwpc.sim_diff(S_u, S_f, N_r, pos[i], T_c)
        if rivelazione == 1:
            tempi.append(tempo)
        rivelazioni = rivelazioni + rivelazione
    tempi = np.array(tempi)
    n_r = rivelazioni
    event = evento(n_c, n_r, tempi, pos)
    arr_eventi.append(event)


arr_eventi = np.array(arr_eventi)
arr_cariche_riv = []
tempi_tot = np.empty(0)
tempi_min = []
tempi_medi = []

for event in arr_eventi:
    arr_cariche_riv.append(event.n_riv)
    tempi_tot = np.concatenate((tempi_tot, event.td_riv))
    if len(event.td_riv) != 0:
        tempi_min.append(min(event.td_riv))
    else:
        tempi_min.append(0)
    if len(event.td_riv) != 0:    
        tempi_medi.append(np.mean(event.td_riv))
    else:
        tempi_medi.append(0)

arr_cariche = np.array(arr_cariche_riv)
tempi_min = np.array(tempi_min)
tempi_medi = np.array(tempi_medi)


eff = []
for i in range(0, len(arr_eventi)):
    if arr_eventi[i].n_gen != 0:
        effi = arr_eventi[i].n_riv/arr_eventi[i].n_gen* 100
    else:
        effi = '0 su 0'
    eff.append(effi)
eff = np.array(eff)

Risultati = pd.DataFrame(columns = ['Particella', 'N. Coppie generate', 'N. elettroni rivelati', 'Efficienza di rivelazione elettroni (%)', 'Tempo di deriva medio', 'Tempo di deriva minimo'])
Risultati['Particella'] = np.arange(1, N_part +1)
Risultati['N. Coppie generate'] = [ev.n_gen for ev in arr_eventi]
Risultati['N. elettroni rivelati'] = [ev.n_riv for ev in arr_eventi]
Risultati['Efficienza di rivelazione elettroni (%)'] = eff
Risultati['Tempo di deriva medio'] = tempi_medi
Risultati['Tempo di deriva minimo'] = tempi_min

print(Risultati)


count = 0
countass = 0
for i in range(0, len(arr_eventi)):
    if arr_eventi[i].n_riv != 0:
        count = count + 1
    else:
        countass = countass + 1


print('Efficienza di rivelazione particelle: ', count / N_part * 100, '%')


plt.figure(figsize = (18, 9))
plt.hist(arr_cariche_riv, bins = 100, color = "rebeccapurple")
plt.xlabel('N cariche rivelate', fontsize = 20)
plt.ylabel("N eventi", fontsize = 20)
plt.title('Distribuzione cariche rilevate', fontsize = 20)
plt.show()

plt.figure(figsize = (18, 9))
plt.hist(tempi_tot[tempi_tot != 0], bins = 100, color = "rebeccapurple")
plt.xlabel('Tempi di deriva', fontsize = 20)
plt.ylabel("N eventi", fontsize = 20)
plt.title('Distribuzione tempi di deriva', fontsize = 20)
plt.show()

plt.figure(figsize = (18, 9))
plt.hist(tempi_min[tempi_min != 0], bins = 100, color = "rebeccapurple")
plt.xlabel('Tempi di deriva minimi', fontsize = 20)
plt.ylabel("N eventi", fontsize = 20)
plt.title('Distribuzione tempi di deriva minimi per particella', fontsize = 20)
plt.show()

plt.figure(figsize = (18, 9))
plt.hist(tempi_medi[tempi_medi != 0], bins = 100, color = "rebeccapurple")
plt.xlabel('Tempi di deriva medi', fontsize = 20)
plt.ylabel("N eventi", fontsize = 20)
plt.title('Distribuzione tempi di deriva medi per particella', fontsize = 20)
plt.show()

