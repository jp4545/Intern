 
import cv2
 
face_cascade = cv2.CascadeClassifier('cascade.xml')
eye_cascade = cv2.CascadeClassifier('n.xml')
vc = cv2.VideoCapture(0)
 
if vc.isOpened():
    rval , frame = vc.read()
else:
    rval = False
 
while rval:
    rval, frame = vc.read()
    gray = cv2.cvtColor(frame,cv2.IMREAD_COLOR)
    cars = face_cascade.detectMultiScale(frame, 1.1, 2)
    for (x,y,w,h) in cars:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
        f = gray[ y:y+h, x:x+w ]
        r = frame[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(f,1.1,2)
        for(ex,ey,ew,eh) in eyes:
          cv2.rectangle(r, (ex,ey), (ex+ew, ey+eh), (0,255,255), 2)
          cv2.imwrite("user.jpg", frame)
          cv2.waitKey(300)
          cv2.imshow("CAPTURED PHOTO",frame)         
    cv2.imshow("Result",frame)
    cv2.waitKey(1);
vc.release()