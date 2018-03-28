import struct
from atmosphere_random import random_ints


WIDTH = 128
HEIGHT = 128
SIZE = 14 + 12 + 128*128*3

imdata = random_ints(HEIGHT * WIDTH * 3, 0, 255)


# build header
header = 'BM'
header += struct.pack('<L', SIZE)
header += struct.pack('<H', 0)
header += struct.pack('<H', 0)
header += struct.pack('<L', 26)

DIB_header = struct.pack('<L', 12)
DIB_header += struct.pack('<h', WIDTH)
DIB_header += struct.pack('<h', -HEIGHT)
DIB_header += struct.pack('<h', 1)
DIB_header += struct.pack('<h', 24)

with open('rand.bmp', 'w+') as img:
        img.write(header + DIB_header + bytearray(imdata))
