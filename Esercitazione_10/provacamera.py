import numpy as np
import ctypes
import matplotlib.pyplot as plt
import matplotlib.colors as color
import sys,os



import mycamera

MAX_STR = 1536 * 1024 * 2


#a = ctypes.create_string_buffer(MAX_STR).from_bytes(b'\xfc\x00', byteorder='big', signed=True)

a = mycamera.read_camera(MAX_STR)

#interi = int.from_bytes(a,  byteorder='big', signed=True)

print(len(a), MAX_STR)

#aa = a[:5]
##print(aa)

ar1 = []
ar2 = []



#for elem in a:

width  = 1536
height = 1024
photo = np.zeros((height, width))

x = -1
y = -1
  
pixel_value = -1
	


#for(int i=0; i<imsize; i+=2){
for i in range(0, len(a), 2):

    x = (i / 2) % width
    y = (i / 2) / width
    a1 = a[i]
    a2 = a[i+1]
    pixel_value = int.from_bytes(a1+a2,  byteorder='little', signed=False)
    photo[int(y)][int(x)] = pixel_value


plt.imshow(photo, cmap = 'turbo', origin = 'lower')
plt.show()