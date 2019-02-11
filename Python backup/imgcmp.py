
'''
Jaya Prakash - 33
Image compare
Not Working
'''
from PIL import Image
import math, operator
def compare(file1, file2):
	 image1 = Image.open("/home/Jp/jp.jpg")
	 image2 = Image.open("/home/Jp/sjp.jpg")
	 h1 = image1.histogram()
	 h2 = image2.histogram()
	 rms = math.sqrt(reduce(operator.add,map(lambda a,b: (a-b)**2, h1, h2))/len(h1))
	 return rms

	 if __name__=='__main__':
	 	 import sys
	 	 file1, file2 = sys.argv[1:]
 		 print(compare(file1, file2))