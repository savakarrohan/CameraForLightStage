# Message Sender
import os, math
from socket import *
from time import sleep

# set to IP address of target computer
host = "192.168.0.111" 
port = 19000
addr = (host, port)
UDPSock = socket(AF_INET, SOCK_DGRAM)
i = 0
while(1):
    val=1
   # val = abs(math.sin(i)) * 1000
    string1 = str(val)
    
    UDPSock.sendto(string1.encode(), addr)
    i = i+0.05
    sleep(0.03)

UDPSock.close()
