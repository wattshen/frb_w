#!/usr/bin/env python


from socket import *
from time import ctime

HOST = ''
PORT = 21567
BUFSIZE = 1024
ADDR = (HOST, PORT)

tcpSersock =  socket(AF_INET, SOCK_STREAM)
tcpSersock.bind(ADDR)
tcpSersock.listen(5)

while True:
	print 'waittng for connecting...'
	tcpClisocket, addr = tcpSersock.accept()
	print '...connected from: %s ,on %s' % (addr, ctime())
	i = 0
	while True:
		data = tcpClisocket.recv(BUFSIZE)
		if not data:
			print 'End on %s' % ctime()
			break
		print 'Query %s at %s' % (i, ctime())
		i = i + 1
		tcpClisocket.send('[%s] %s' % (ctime(),data))
	tcpClisocket.close()
tcpSersock.close()