'''
Jaya Prakash - 33
Image in List format
Working
'''
from PIL import Image
im = Image.open('test.png')
pixels=[] 
pixels= list(im.getdata())
n = len(pixels)
for i in range(0,n):
	  print(pixels[i])