#!/usr/bin/python
import socket
ip = raw_input("Enter the IP:")
port = input("Enter the PORT:")
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
if s.connect_ex((ip,port)):
     print "Port",port,"is close"
else:
     print "Port",port,"is open"
