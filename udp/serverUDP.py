import socket
import os

UDP_IP ="127.0.0.1"
UDP_PORT = 3008

sock_server = socket.socket(socket.AF_INET, # Internet
                    socket.SOCK_DGRAM) # UDP
					
sock_client = socket.socket(socket.AF_INET, # Internet
                    socket.SOCK_DGRAM) # UDP
                     
# Faz o bind local. Associa um socket com um IP e uma Porta.
sock_server.bind((UDP_IP, UDP_PORT))

while True:
	message, addr = sock_server.recvfrom(1024) # Tamanho do buffer eh 1024 bytes
	sock_client.sendto(message, addr) # Resposta do server para calcular latencia (RTT)

sock_client.close()
sock_server.close()

