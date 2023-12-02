import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

file1 = pd.read_csv('hit_times_M0.csv')
file2 = pd.read_csv('hit_times_M1.csv')
file3 = pd.read_csv('hit_times_M2.csv')
file4 = pd.read_csv('hit_times_M3.csv')

print(file1)

n, bins, p = plt.hist(file1['hit_time'], bins=150, color='royalblue', alpha=0.7 )
plt.xlabel('tempo (s) ', fontsize=14)
plt.ylabel('N hit ', fontsize=14)
plt.show()

differenze = np.diff(file1['hit_time'])
mask_diff = differenze != 0 

n_diff, bins_diff, p_diff = plt.hist(np.log10(differenze[mask_diff]), bins=150, color='royalblue', alpha=0.7 )
plt.xlabel('tempo (s) ', fontsize=14)
plt.ylabel('N hit', fontsize=14)
plt.show()
