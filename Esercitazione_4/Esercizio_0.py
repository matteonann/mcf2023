import numpy as np
import sys,os

sys.path.append('somme.py')
sys.path

import somme

somma_3 = somme.somma(3)
somma_3_sqrt = somme.somma_radici(3)
sommaprod_3 = somme.somma_prodotto(3)
somma_3_quad = somme.somma_potenza(3, 2)

print('La somma dei primi 3 numeri è ', somma_3)
print('La somma delle prime 3 radici quadrate è ', somma_3_sqrt)
print('La somma e il prodotto dei primi 3 numero sono ',  sommaprod_3[0], ' e ', sommaprod_3[1])
print('La somma dei primi 3 quadrati è ', somma_3_quad)
