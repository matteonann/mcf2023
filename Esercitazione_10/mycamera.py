import numpy as np
import ctypes



# Carico la lireria libserie (libserie.so) che è presente nella cartella di lavoro  ('.')
_libmycamera = np.ctypeslib.load_library('libmycamera', '.')

# definizoine tipi di input (argtypes) e di output (restypes) per la funzione sum_n di libserie 
_libmycamera.read_camera.argtypes = [ctypes.c_char_p]
_libmycamera.read_camera.restype  = ctypes.c_int




# utilizzo di _libserie.sum_n
# il parametro n va necessariamente convertito in int
def read_camera(MAX_STR):
    a = ctypes.create_string_buffer(MAX_STR)
    _libmycamera.read_camera(a)
    return a
