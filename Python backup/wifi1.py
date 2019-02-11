import socket
import time
HOST = "192.168.43.175"

PORT = 5454
data = "Some text"

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect((HOST,PORT))
while True:
	s.sendto(data,(HOST,PORT))
	print ("send: "+ data)
	time.sleep(1)