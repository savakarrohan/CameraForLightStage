# Message Sender
from socket import *
from time import sleep

# set to IP address of target computer
host1 = "192.168.1.210" 
port1 = 19000
addr1 = (host1, port1)
UDPSock1 = socket(AF_INET, SOCK_DGRAM)

host2 = "192.168.1.115" 
port2 = 19000
addr2 = (host2, port2)
UDPSock2 = socket(AF_INET, SOCK_DGRAM)

print(" c: Capture Image \n a: Calibration Image\n q: Exit\n Please do not send more than 1 command each time")
while True:
    IncomingChar = input()         #For input of the character
    if  IncomingChar == 'c' :   #This is going to be used for the capture
        string1 = 'c'
        print("Taken Image of object")
        UDPSock1.sendto(string1.encode(), addr1)
        UDPSock2.sendto(string1.encode(), addr2)
        sleep(1)
        
    if  IncomingChar == 'a' :    #This is going to be used for calibration
        string1 = 'a'
        print("Taken Calibration capture")
        UDPSock1.sendto(string1.encode(), addr1) #This is to quit the system
        UDPSock2.sendto(string1.encode(), addr2)
        sleep(1)
        
    if IncomingChar == 'q':
        break

UDPSock1.close()
