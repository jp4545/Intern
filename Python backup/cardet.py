# -------------------- THIS IS USED TO CAPTURE STORE THE PHOTOS TO TRAIN THE FACE RECOGNITION SYSTEMS ------------------
# ------------SPECIAL ADDITIONS ARE MADE TO SAVE IMAGES ONLY WITH CORRECT ILLUMINATION AND CORRECT TILTED HEADS---------
# ------------------------------ CREATED BY LAHIRU DINALANKARA - AKA SPIKE ---------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------

import cv2                  # Importing the opencv
import numpy as np          # Import Numarical Python
import NameFind2
from decimal import Decimal
WHITE = [255, 255, 255]

#   import the Haar cascades for face ditection

num_cascade = cv2.CascadeClassifier('cars.xml')


ID = NameFind2.AddName()
#NameFind1.Checkid(ID)
Count = 0
cap = cv2.VideoCapture(0)                                                                           # Camera object

while Count < 50:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)                                                    # Convert the Camera to graySe
    if np.average(gray) > 110:                                                                      # Testing the brightness of the image
        faces = num_cascade.detectMultiScale(gray, 1.3, 5)                                         # Detect the faces and store the positions
        for (x, y, w, h) in faces:                                                                  # Frames  LOCATION X, Y  WIDTH, HEIGHT
            FaceImage = gray[y - int(h / 2): y + int(h * 1.5), x - int(x / 2): x + int(w * 1.5)]    # The Face is isolated and cropped
            Img = (NameFind2.DetectEyes(FaceImage))
            cv2.putText(gray, "Car DETECTED",(x+(w//2),y-5), cv2.FONT_HERSHEY_DUPLEX, .4, WHITE)
            #tc1 = img_as_ubyte(tc)
            #print(tc)
            #cv2.putText(tc)           
            if Img is not None:
                frame = Img                                                                         # Show the detected faces
            else:
                frame = gray[y: y+h, x: x+w]
            cv2.imwrite("dataSet1/user." + str(ID) + "." + str(Count) + ".jpg", frame)
            cv2.waitKey(300)
            cv2.imshow("CAPTURED PHOTO", frame)                                                     # show the captured image
            Count = Count + 1
    cv2.imshow('Car Recognition System Capture Faces', gray)                                       # Show the video
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
print('Car CAPTURE FOR THE SUBJECT IS COMPLETE')
cap.release()
cv2.destroyAllWindows()