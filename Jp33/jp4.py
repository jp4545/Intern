'''
Jaya Prakash - 33
Image as array
Working
'''
from PIL import Image
import numpy as np
im = Image.open('jp.jpg')
pix = np.asarray(im)
print(pix)