import cv2 
import math
import time


def AddName():
    Name = input('Enter Your Name ')
    Info = open("Names.txt", "r+")
    ID = ((sum(1 for line in Info))+1)
    Info.write(str(ID) + "," + Name + "\n")
    print ("Name Stored in " + str(ID))
    Info.close()
    return ID