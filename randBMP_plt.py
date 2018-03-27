import numpy as np
from matplotlib import pyplot as plt
from atmosphere_random import random_ints

WIDTH = 128
HEIGHT = 128


imdata = np.array(random_ints(HEIGHT * WIDTH * 3), dtype=np.ubyte).reshape(HEIGHT, WIDTH, 3)
plt.imsave(imdata, format='bmp')
