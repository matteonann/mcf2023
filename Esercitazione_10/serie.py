import numpy as np
import ctypes

# Carico la lireria libserie (libserie.so) che è presente nella cartella di lavoro  ('.')
_libserie = np.ctypeslib.load_library('libserie', '.')

# definizoine tipi di input (argtypes) e di output (restypes) per la funzione sum_n di libserie 
_libserie.fibonacci.argtypes = [ctypes.c_int]
_libserie.fibonacci.restype  = ctypes.c_double




# utilizzo di _libserie.sum_n
# il parametro n va necessariamente convertito in int
def fibonacci(n):
    return _libserie.fibonacci(int(n))


