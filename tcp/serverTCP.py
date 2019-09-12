#!/usr/bin/env python

import socket
import time

CHUNK_SIZE = 10 * 1024

TCP_IP = '127.0.0.1'
TCP_PORT = 5006

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)
 

#print 'Endereco de conexao: ', addr
while True:
	erro = False
	conn, addr = s.accept()
	data = conn.recv(CHUNK_SIZE) #Tamanho do buffer.
	cont = 0
	while (data and not erro):
		cont = cont + 1
		print cont
		print "Mensagem Recebida:", data
		#message = data.upper()
		try:
			conn.send(data)  # echo
			data = conn.recv(CHUNK_SIZE) #Tamanho do buffer.
		except socket.error, ex:
			print "ERRO"
			erro = True
	conn.close()
