# -*- coding: utf-8 -*-
"""
Created on Wed Dec 26 17:04:11 2018

@author: NoPo VR 2
"""

import os
from socket import *
import struct
host = ""
port = 19000
buf = 2048
addr = (host, port)
UDPSock = socket(AF_INET, SOCK_DGRAM)
UDPSock.bind(addr)
#file = open("DataV3.txt", "w")
print("Waiting to receive messages...")
while True:
    (data, addr) = UDPSock.recvfrom(buf)
    #print("Received message: " + data)
    # print(data)
    print("data: \n" + str(data), end="")
    #file.write(str(data)+"\n")
    #if data == "exit":
    #    break
UDPSock.close()
os._exit(0)
#file.close()
