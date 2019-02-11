import cv2
import NameFind4

ID = NameFind4.AddName()


cv2.namedWindow("test")


cam = cv2.VideoCapture(0)


img_counter = 0
count = 0

while count <= 50:
    ret, frame = cam.read()
    cv2.imshow("test", frame)
    if not ret:
        break
    k = cv2.waitKey(1)

    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        # SPACE pressed
        img_name = "dataset/user.{}"+ str(ID) + "." + str(count) + ".jpg"
        img_name1 = img_name.format(count)

        cv2.imwrite(img_name1,frame)
        cv2.waitKey(300)
                                                         # show the captured image
        count = count + 1
        
        #cv2.imwrite(img_name, frame)
        #print("{} written!".format(img_name))
        #img_counter += 1

cam.release()

cv2.destroyAllWindows()
