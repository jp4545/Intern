import cv2                  # Importing the opencv
import numpy as np          # Import Numarical Python
import NameFind3
from decimal import Decimal



face_cascade = cv2.CascadeClassifier('cars.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_russian_plate_number.xml')

ID = NameFind3.AddName()
Count = 0
cap = cv2.VideoCapture(0)
cap.set(3, 640) #WIDTH
cap.set(4, 480) #HEIGHT


while Count < 50:
    # Capture frame-by-frame
  ret, frame = cap.read()

    # Our operations on the frame come here
  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  if np.average(gray) > 110:   
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    print(len(faces))
    # Display the resulting frame
    for (x,y,w,h) in faces:
         cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
         roi_gray = gray[y:y+h, x:x+w]
         roi_color = frame[y:y+h, x:x+w]
         eyes = eye_cascade.detectMultiScale(roi_gray)
         for (ex,ey,ew,eh) in eyes:
             cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
             FaceImage = gray[ey - int(eh / 2): ey + int(eh * 1.5), ex - int(ex / 2): ex + int(ew * 1.5)]    # The Face is isolated and cropped
             Img = (NameFind3.DetectEyes(FaceImage))
             #cv2.putText(gray, "Numplate DETECTED",(ex+(ew//2),ey-5), cv2.FONT_HERSHEY_DUPLEX, .4, WHITE)

             if Img is  not None:
                frame = Img
             else:
                frame = gray[ey: ey+eh, ex: ex+ew]
             cv2.imwrite("dataSet/user." + str(ID) + "." + str(Count) + ".jpg", frame)
             cv2.waitKey(300)
             cv2.imshow("CAPTURED PHOTO", frame)                                                     # show the captured image
             Count = Count + 1
    #cv2.imshow('Numplate Recognition System Capture Faces', gray)   

  cv2.imshow('frame',frame)
  if cv2.waitKey(1) & 0xFF == ord('q'):
      break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()