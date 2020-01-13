#!/usr/bin/python
import socket
c=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
while True:
	x=raw_input("enter the command:")
	c.sendto(x,("192.168.221.129",2336))
	


