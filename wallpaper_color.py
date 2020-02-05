from __future__ import print_function
import binascii
import struct
from PIL import Image
import numpy as np
import scipy
import scipy.misc
import scipy.cluster
import os

NUM_CLUSTERS = 5
fehbg = open('/home/gerontius/.fehbg')
fehbg.readline() #discard first line
wallpapers = fehbg.readline()
currentWallpaper = wallpapers.split("'")[1]

# print(fehbg) 

# print('reading image')
im = Image.open(currentWallpaper)
im = im.resize((50, 50))      
ar = np.asarray(im)
shape = ar.shape
ar = ar.reshape(scipy.product(shape[:2]), shape[2]).astype(float)

# print('finding clusters')
codes, dist = scipy.cluster.vq.kmeans(ar, NUM_CLUSTERS)
# print('cluster centres:\n', codes)

vecs, dist = scipy.cluster.vq.vq(ar, codes)         # assign codes
counts, bins = scipy.histogram(vecs, len(codes))    # count occurrences

index_max = scipy.argmax(counts)                    # find most frequent
peak = codes[index_max]
colour = binascii.hexlify(bytearray(int(c) for c in peak)).decode('ascii')
print(colour)
cmd ='ratbagctl warbling-mara led 0 set color '+ 'd37f8b'
#
os.system(cmd)
