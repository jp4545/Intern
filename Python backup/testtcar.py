#!/usr/bin/env python

# Python 2/3 compatibility
from __future__ import print_function

import numpy as np
import cv2
import NameFind1
from decimal import Decimal
WHITE = [255, 255, 255]


car_cascade = cv2.CascadeClassifier('cascade_dir/cascade.xml')
ID = NameFind1.AddName()
count = 0
cap = cv2.VideoCapture(0)


while count <= 50:
        flag, img = cap.read()
        #if img == None: break

        height, width, c = img.shape
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        if np.average(gray) > 110:
                cars = car_cascade.detectMultiScale(gray, 1.2, 5)
        for (x,y,w,h) in cars:
            CarImage = gray[y - int(h / 2): y + int(h * 1.5), x - int(x / 2): x + int(w * 1.5)]    # The Face is isolated and cropped
            Img = (NameFind1.DetectEyes(CarImage))
            cv2.putText(gray, "CAR DETECTED",(x+(w//2),y-5), cv2.FONT_HERSHEY_DUPLEX, .4, WHITE)
            if Img is not None:
                frame = Img                                                                         # Show the detected faces
            else:
                frame = gray[y: y+h, x: x+w]
            cv2.imwrite("dataSet/user." + str(ID) + "." + str(Count) + ".jpg", frame)
            cv2.waitKey(300)
            cv2.imshow("CAPTURED PHOTO", frame)                                                     # show the captured image
            Count = Count + 1
        cv2.imshow('Numplate Recognition System Capture Faces', gray)                       

    step = False
    ch = cv2.waitKey(5)
    if ch == 13:
        step = True
    if ch == 32:
        paused = not paused
    if ch == 27:
        break
cap.release()
cv2.destroyAllWindows()