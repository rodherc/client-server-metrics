#!/usr/bin/env python

import socket
import time


def to_miliseconds(seconds): # Transforma segundos em milisegundos
	return round(seconds * 1000,4) # Arredondamento com 4 casas
	
CHUNK_SIZE = 10 * 1024

tcp_ip = '192.168.105.54'
tcp_port = 5006

s = socket.socket(socket.AF_INET,
				socket.SOCK_STREAM)
s.connect((tcp_ip, tcp_port))

arquivo = open("entrada.txt") 
cont = 0


message = arquivo.read(CHUNK_SIZE)


start = time.time() # Momento em que a mensagem e enviada
tam = 0
while message:
	s.send(message)
	
	data = s.recv(CHUNK_SIZE) #Tamanho do buffer.
	tam = tam + len(data)
	cont = cont + 1
	print cont
	print "Mensagem recebida: ", data
	
	message = arquivo.read(CHUNK_SIZE)
	
end = time.time()   # Momento em que a resposta do server e recebida
rtt = end - start

arquivo.close()
arquivo = open("entrada.txt")

tamMessage = arquivo.read()
tamMessage = len(tamMessage)
arquivo.close()
print "Tamanho enviado e recebido :" , tam 
print "Tamanho Mensagem :", tamMessage
print "Latencia (RTT): "+ str(to_miliseconds(rtt)) + " ms"
print "Vazao :" + str(round((tam/rtt) /  1048576,4)) + " MB/s"

s.close()
