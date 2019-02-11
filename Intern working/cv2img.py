import cv2
import numpy as np
import pytesseract
from PIL import Image

src_path = "Desktop"

def get_String(img_path):
	  img = cv2.readimread(img_path)
	  img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	  kernel = np.ones(1,1),np.uint8
	  img = cv2.dilate(img,kernel,iterations=1)
	  img = cv2.erode(img, kernel, iterations=1)
	  cv2.imwrite(src_path + "removed_noise.png", img)
	  img = cv2.adaptiveTreshold(img, 255, img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2))
	  cv2.imwrite(src_path + "thres.png", img)

	  result = pytesseract.image_to_string(Image.open(src_path + "thres.png"))

      return result


print '--- Start recognize text from image ---'
print get_string(src_path + "ja.png")

print "------ Done -------"
