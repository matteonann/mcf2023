import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as color
import sys,os

sys.path.append('randomwalk2d.py')
sys.path

import randomwalk2d

#produrre un grafico 2D delle posizioni di 5 random walker per 1000 passi

N = 1000
s = input('Inserire il passo: ')
s = float(s)

rwx_1, rwy_1 = randomwalk2d.random_walk2d(s, N)

rwx_2, rwy_2 = randomwalk2d.random_walk2d(s, N)

rwx_3, rwy_3 = randomwalk2d.random_walk2d(s, N)

rwx_4, rwy_4 = randomwalk2d.random_walk2d(s, N)

rwx_5, rwy_5 = randomwalk2d.random_walk2d(s, N)

plt.figure(figsize = (18, 9))
plt.title('Random walk simmetrico', fontsize = 20)
plt.plot(rwx_1, rwy_1, color = 'royalblue', label = 'r.w. 1')
plt.plot(rwx_2, rwy_2, color = 'mediumseagreen', label = 'r.w. 2')
plt.plot(rwx_3, rwy_3, color = 'crimson', label = 'r.w. 3')
plt.plot(rwx_4, rwy_4, color = 'sandybrown', label = 'r.w. 4')
plt.plot(rwx_5, rwy_5, color = 'rebeccapurple', label = 'r.w. 5')
plt.legend(fontsize = 20)
plt.xlabel('x (u.a.)', fontsize = 20)
plt.ylabel('y (u.a.)', fontsize = 20)
plt.show()

#produrre un grafico 2D della posizione di 100 random walker dopo 10, 100 e 1000 passi;

fig, ax = plt.subplots(1, 3, figsize = (18, 9))
ax[0].set_title('10 passi', fontsize = 20)
ax[0].set_xlabel('x (u.a.)', fontsize = 20)
ax[0].set_ylabel('y (u.a.)', fontsize = 20)

ax[1].set_title('100 passi', fontsize = 20)
ax[1].set_xlabel('x (u.a.)', fontsize = 20)
ax[1].set_ylabel('y (u.a.)', fontsize = 20)

ax[2].set_title('1000 passi', fontsize = 20)
ax[2].set_xlabel('x (u.a.)', fontsize = 20)
ax[2].set_ylabel('y (u.a.)', fontsize = 20)

for i in range(0, 100):
    rwx, rwy = randomwalk2d.random_walk2d(s, 1000)
    ax[0].scatter(rwx[10], rwy[10], color = 'royalblue')
    ax[1].scatter(rwx[100], rwy[100], color = 'crimson')
    ax[2].scatter(rwx[1000], rwy[1000], color = 'mediumseagreen')


plt.show()

#prdurre ung grafico con due pannelli che mostri:
#nel primo pannello lo stesso grafico del punto A;
#nel secondo pannello il quadrato della distanza dal punto di partenza in 
#funzione dei passi per gli stessi 5 random walker.


fig, ax = plt.subplots(1, 2, figsize = (18, 9))
ax[0].plot(rwx_1, rwy_1, color = 'royalblue', label = 'r.w. 1')
ax[0].plot(rwx_2, rwy_2, color = 'mediumseagreen', label = 'r.w. 2')
ax[0].plot(rwx_3, rwy_3, color = 'crimson', label = 'r.w. 3')
ax[0].plot(rwx_4, rwy_4, color = 'sandybrown', label = 'r.w. 4')
ax[0].plot(rwx_5, rwy_5, color = 'rebeccapurple', label = 'r.w. 5')
ax[0].legend(fontsize = 20)
ax[0].set_xlabel('x (u.a.)', fontsize = 20)
ax[0].set_ylabel('y (u.a.)', fontsize = 20)
ax[0].set_title('Posizioni')

ax[1].set_title('Distanze dall origine', fontsize = 20)
ax[1].set_xlabel('x (u.a.)', fontsize = 20)
ax[1].set_ylabel('y (u.a.)', fontsize = 20)
ax[1].plot(np.sqrt(rwx_1**2 + rwy_1**2), color = 'royalblue', label = 'r.w. 1')
ax[1].plot(np.sqrt(rwx_2**2 + rwy_2**2), color = 'mediumseagreen', label = 'r.w. 2')
ax[1].plot(np.sqrt(rwx_3**2 + rwy_3**2), color = 'crimson', label = 'r.w. 3')
ax[1].plot(np.sqrt(rwx_4**2 + rwy_4**2), color = 'sandybrown', label = 'r.w. 4')
ax[1].plot(np.sqrt(rwx_5**2 + rwy_5**2), color = 'rebeccapurple', label = 'r.w. 5')
ax[1].legend(fontsize = 20)

plt.show()


#asimmetrica


rwx_1_as, rwy_1_as = randomwalk2d.random_walk2d_as(s, N)

rwx_2_as, rwy_2_as = randomwalk2d.random_walk2d_as(s, N)

rwx_3_as, rwy_3_as = randomwalk2d.random_walk2d_as(s, N)

rwx_4_as, rwy_4_as = randomwalk2d.random_walk2d_as(s, N)

rwx_5_as, rwy_5_as = randomwalk2d.random_walk2d_as(s, N)

plt.figure(figsize = (18, 9))
plt.title('Random walk asimmetrico', fontsize = 20)
plt.plot(rwx_1_as, rwy_1_as, color = 'royalblue', label = 'r.w. 1')
plt.plot(rwx_2_as, rwy_2_as, color = 'mediumseagreen', label = 'r.w. 2')
plt.plot(rwx_3_as, rwy_3_as, color = 'crimson', label = 'r.w. 3')
plt.plot(rwx_4_as, rwy_4_as, color = 'sandybrown', label = 'r.w. 4')
plt.plot(rwx_5_as, rwy_5_as, color = 'rebeccapurple', label = 'r.w. 5')
plt.legend(fontsize = 20)
plt.xlabel('x (u.a.)', fontsize = 20)
plt.ylabel('y (u.a.)', fontsize = 20)
plt.show()


#con sf=0.1s

rwx_1_sf_1, rwy_1_sf_1 = randomwalk2d.random_walk2d_sf(s, 0.1*s, N)

rwx_2_sf_1, rwy_2_sf_1 = randomwalk2d.random_walk2d_sf(s, 0.1*s, N)

rwx_3_sf_1, rwy_3_sf_1 = randomwalk2d.random_walk2d_sf(s, 0.1*s, N)

rwx_4_sf_1, rwy_4_sf_1 = randomwalk2d.random_walk2d_sf(s, 0.1*s, N)

rwx_5_sf_1, rwy_5_sf_1 = randomwalk2d.random_walk2d_sf(s, 0.1*s, N)

plt.figure(figsize = (18, 9))
plt.title('Random walk simmetrico con sf = 0.1*s', fontsize = 20)
plt.plot(rwx_1_sf_1, rwy_1_sf_1, color = 'royalblue', label = 'r.w. 1')
plt.plot(rwx_2_sf_1, rwy_2_sf_1, color = 'mediumseagreen', label = 'r.w. 2')
plt.plot(rwx_3_sf_1, rwy_3_sf_1, color = 'crimson', label = 'r.w. 3')
plt.plot(rwx_4_sf_1, rwy_4_sf_1, color = 'sandybrown', label = 'r.w. 4')
plt.plot(rwx_5_sf_1, rwy_5_sf_1, color = 'rebeccapurple', label = 'r.w. 5')
plt.legend(fontsize = 20)
plt.xlabel('x (u.a.)', fontsize = 20)
plt.ylabel('y (u.a.)', fontsize = 20)
plt.show()



#con sf=0.01s

rwx_1_sf_01, rwy_1_sf_01 = randomwalk2d.random_walk2d_sf(s, 0.01*s, N)

rwx_2_sf_01, rwy_2_sf_01 = randomwalk2d.random_walk2d_sf(s, 0.01*s, N)

rwx_3_sf_01, rwy_3_sf_01 = randomwalk2d.random_walk2d_sf(s, 0.01*s, N)

rwx_4_sf_01, rwy_4_sf_01 = randomwalk2d.random_walk2d_sf(s, 0.01*s, N)

rwx_5_sf_01, rwy_5_sf_01 = randomwalk2d.random_walk2d_sf(s, 0.01*s, N)



plt.figure(figsize = (18, 9))
plt.title('Random walk simmetrico con sf = 0.01*s', fontsize = 20)
plt.plot(rwx_1_sf_01, rwy_1_sf_01, color = 'royalblue', label = 'r.w. 1')
plt.plot(rwx_2_sf_01, rwy_2_sf_01, color = 'mediumseagreen', label = 'r.w. 2')
plt.plot(rwx_3_sf_01, rwy_3_sf_01, color = 'crimson', label = 'r.w. 3')
plt.plot(rwx_4_sf_01, rwy_4_sf_01, color = 'sandybrown', label = 'r.w. 4')
plt.plot(rwx_5_sf_01, rwy_5_sf_01, color = 'rebeccapurple', label = 'r.w. 5')
plt.legend(fontsize = 20)
plt.xlabel('x (u.a.)', fontsize = 20)
plt.ylabel('y (u.a.)', fontsize = 20)
plt.show()


