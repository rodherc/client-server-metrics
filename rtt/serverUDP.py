import socket
import os

udp_ip = "127.0.0.1"
udp_port = 4004

#udp_ip_send = "127.0.0.1"
udp_port_send = 3003

sock_server = socket.socket(socket.AF_INET, # Internet
                    socket.SOCK_DGRAM) # UDP
					
sock_client = socket.socket(socket.AF_INET, # Internet
                    socket.SOCK_DGRAM) # UDP
                     
# Faz o bind local. Associa um socket com um IP e uma Porta.
sock_server.bind((udp_ip, udp_port))

while True:
	message, addr = sockS.recvfrom(1024) # Tamanho do buffer eh 1024 bytes
	print message
	sock_client.sendto(message + " foi recebida", (addr[0], udp_port_send)) # Resposta do server para calcular latencia (RTT)

sock_client.close()
sock_server.close()

