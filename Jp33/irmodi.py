'''
Jaya Prakash-33
10-5-18
Working
IR sensor working
'''
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(16,GPIO.IN)
GPIO.setup(25,GPIO.IN)
count = 0
while True:
	  if GPIO.input(16)==False and GPIO.input(25)==True:
	        print("One person coming in")
                time.sleep(0.5)
	        if GPIO.input(25)==False and GPIO.input(16)==True:
	            count = count+1
	            print("One person in")
	            print(count)
 	            if(count>0):
	                GPIO.output(18,True)
	        time.sleep(1)
	  if GPIO.input(25)==False and GPIO.input(16)==True:
	          print("One person coming out")
	          time.sleep(0.5)
		  if GPIO.input(16)==False and GPIO.input(25)==True:
	              count = count-1
	              print("One person is out")
	              print(count)
	              if(count<=0):
		         GPIO.output(18,False)
	          time.sleep(1)
