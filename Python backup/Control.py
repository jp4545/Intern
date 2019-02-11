
# coding: utf-8

# In[ ]:

import socket               
 
# Create a socket object
s = socket.socket()         
 

# Define the port on which you want to connect
port = int(input("Enter Port Number: "))             
 
# connect to the server on local computer 192.168.43.193
s.connect(('192.168.137.107', port))
 
# receive data from the server
print(s.recv(1024))

print ("1.Start \n 2. Forward \n 3. Reverse \n 4.Turn Left \n 5.Turn Right \n 6. Stop \n 0.EXIT")


message = input(" -> ")  # take input
while message != '0':
        s.send(message.encode())  # send message
        #data = s.recv(1024).decode()  # receive response
        #print('Received from server: ' + data)  # show in terminal
        message = input(" -> ")  # again take input

s.send(message.encode())	
# close the connection
s.close()


# In[ ]:



