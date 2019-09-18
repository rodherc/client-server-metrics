#!/usr/bin/env python

import socket
import time
import os

TCP_IP = '192.168.104.13'
TCP_PORT = 5006

sock = socket.socket(socket.AF_INET,
				socket.SOCK_STREAM)
sock.connect((TCP_IP, TCP_PORT))

arquivo = open("entrada.txt") 
message = arquivo.read(1024)
start = time.time() # Momento em que a mensagem e enviada

while message:
	sock.send(message)
	message = arquivo.read(1024)

end = time.time()   # Momento em que a resposta do server e recebida
rtt = end - start

tam = os.path.getsize('entrada.txt')
print "\n               --- Estatisticas --- \n"
print "Tamanho Mensagem:",tam, "bytes"
print "Latencia (RTT): ", round(rtt * 1000,4), "ms"
print "Vazao:", round((8* tam/rtt) /1000000, 4), "Mb/s"

arquivo.close()
sock.close()
