'''
Jaya Prakash - 33
Face Detection-Name storing
Working
'''
import cv2
import numpy as np
import NameFind
#import  ...
WHITE = [255, 255, 255]

face_cascade = cv2.CascadeClassifier('haarcascade_frontalcatface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

ID = NameFind.AddName()
c= 0
cap = cv2.VideoCapture(0)

while c<50:
	ret,img = cap.read()
	gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	if np.average(gray) > 110:	
			faces = face_cascade.detectMultiScale(gray, 1.3, 5)
			for(x, y, w, h) in faces:
				 FaceImage = gray[y - int(h / 2): y + int(h * 1.5), x - int(x / 2): x + int(w * 1.5)]
				 Img = NameFind.DetectEyes(FaceImage)
				 cv2.putText(gray, "Face Detected", (x+(w / 2), y - 5), cv2.FONR_HERSHEY_DUPLEX, .4, WHITE)
				 if Img is not None:
				 	frame = Img
				 else:
				 	frame = gray[y: y + h, x: x + w]
				 	cv2.imwrite("Desktop/user" +  str(ID) + "." +  str(count) + ".jpg", frame)
				 	cv2.waitKey(30)
				 	cv2.imshow("Captured Photo", frame)
				 	c = c + 1
	if cv2.waitKey(1) & 0xff == ord('q'):
		break
print("Face capturing is complete")
cap.release()
cv2.destroyAllWindows()			 	