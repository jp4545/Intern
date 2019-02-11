import os, sys
from PIL import Image

im = Image.open("jp.jpg")
x = 3
y = 4

pix = im.load()
print(pix[x,y])