#!/usr/bin/env python

from socket import *

HOST = 'localhost'
PORT = 21567
BUFSIZE = 1024
ADDR = (HOST, PORT)

tcpClisocket =  socket(AF_INET, SOCK_STREAM)
tcpClisocket.connect(ADDR)

while True:
	data = raw_input('>')
	if not data:
		break
	tcpClisocket.send(data)
	data = tcpClisocket.recv(BUFSIZE)
	if not data:
		break
	print data


tcpClisocket.close()