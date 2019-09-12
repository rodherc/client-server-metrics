#!/usr/bin/env python

import socket
import time

TCP_IP = '192.168.103.7'
TCP_PORT = 5006

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((TCP_IP, TCP_PORT))
sock.listen(1)
 
while True:
	conn, addr = sock.accept()
	data = conn.recv(1024) #Tamanho do buffer.

	while data:
		data = conn.recv(1024) #Tamanho do buffer.

	conn.close()
