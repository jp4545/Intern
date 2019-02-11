import socket
HOST = '192.168.137.142'
PORT = 9876
ADDR = (HOST,PORT)
BUFSIZE = 4096
videofile = "jp.jpg"
bytes = open(videofile).read()
print (len(bytes))
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)
client.send(bytes)
client.close()