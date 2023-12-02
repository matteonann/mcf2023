import sys,os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


sys.path.append('reco.py')
sys.path

import reco

file0 = pd.read_csv('hit_times_M0.csv')
file1 = pd.read_csv('hit_times_M1.csv')
file2 = pd.read_csv('hit_times_M2.csv')
file3 = pd.read_csv('hit_times_M3.csv')

def array_hit(a, b, c):
          hits = []
          for i in range(0, len(a)):
                    hits.append(reco.Hit(a[i], b[i], c[i]))
          return hits

hits_mod_0 = array_hit(file0['mod_id'], file0['det_id'], file0['hit_time'])
hits_mod_1 = array_hit(file1['mod_id'], file1['det_id'], file1['hit_time'])
hits_mod_2 = array_hit(file2['mod_id'], file2['det_id'], file2['hit_time'])
hits_mod_3 = array_hit(file3['mod_id'], file3['det_id'], file3['hit_time'])

hits = []

for elem1, elem2, elem3, elem4 in zip(hits_mod_0, hits_mod_1, hits_mod_2, hits_mod_3):
          hits.append(elem1)
          hits.append(elem2)
          hits.append(elem3)
          hits.append(elem4)


h1 = reco.Hit(1, 2, 3)
h2 = reco.Hit(2, 2, 3)
h3 = reco.Hit(1, 3, 4)
h4 = reco.Hit(1, 2, 4)


hits_numpy = np.array(hits)
hits_sorted = np.sort(hits_numpy)


differenze = np.diff(hits_sorted)

mask_diff = differenze > 0

differenze_mascherate = differenze[mask_diff]

n, bins, p = plt.hist(np.log10(np.float64(differenze_mascherate)), bins = 150, color = 'royalblue')
plt.xlabel('tempi (s)', fontsize=14)
plt.ylabel('N hit', fontsize=14)
plt.yscale('log')
plt.show()

