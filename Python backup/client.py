import socket

# next create a socket object
s = socket.socket()         
print ("Socket successfully created")
 
# reserve a port on your computer in our
# case it is 12345 but it can be anything
port = 12345               
 
s.bind(('', port))        
print ("socket binded to %s" %(port))
 
# put the socket into listening mode
s.listen(5)     
print ("socket is listening")           

# Establish connection with client.
c, addr = s.accept()     
print ('Got connection from', addr)

# send a thank you message to the client. 
#c.send('Thank you for connecting')

#GPIO.output(EN1,GPIO.LOW)
#GPIO.output(EN2,GPIO.LOW)
#pwm1.stop()
#pwm2.stop()
        

text_file = 'unnamed.jpg'

#Send file
with open(text_file, 'rb') as fs: 
    #Using with, no file close is necessary, 
    #with automatically handles file close
    while True:
        data = fs.read(1024)
        print('Sending data', data.decode('utf-8'))
        s.send(data)
        print('Sent data', data.decode('utf-8'))
        if not data:
            print('Breaking from sending data')
            break
    fs.close()

#Receive file
print("Receiving..")
with open(text_file, 'wb') as fw:
    while True:
        data = s.recv(1024)
        if not data:
            break
        fw.write(data)
    fw.close()
print("Received..")
    
c.close()


