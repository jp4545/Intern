'''
Jaya Prakash - 33
Working
Face detection including eye
'''


import cv2
import numpy as np
import NameFindpic

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

count = 0
cap = cv2.VideoCapture(0)
while count <= 10:
 		ret, img = cap.read()
 		gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
 		if np.average(gray) > 100:
 			faces = face_cascade.detectMultiScale(gray, 1.3, 5)
 			for (x,y,w,h) in faces:
				#cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0),2)
 				FaceImage = gray[ y - int(h / 2): y + int(h * 1.5), x - int(x / 2): x + int(w * 1.5) ]
 				roi_gray = gray[ y:y+h, x:x+w ]
 				roi_color = img[y:y+h, x:x+w]
 		    	eyes = eye_cascade.detectMultiScale(roi_gray)
 				for(ex,ey,ew,eh) in eyes:
 			 		cv2.rectangle(roi_color, (ex,ey), (ex+ew, ey+eh), (0,255,0), 2)
 			 		Img = (NameFindpic.DetectEyes(FaceImage))
 			 		if Img is not None:
 			 	 		frame = Img
 			 		else:
                		frame = gray[y: y+h, x: x+w]
            		cv2.imwrite("user." + ".jpg", frame)
            		cv2.waitKey(300)
            		cv2.imshow("CAPTURED PHOTO", frame)                                                     # show the captured image
           			Count = Count + 1

 			#cv2.imshow('img',img) 
 			k = cv2.waitKey(30) & 0xff
 			if k == 27:
 		    	break;
cap.release()
cv2.destroyAllWindows()