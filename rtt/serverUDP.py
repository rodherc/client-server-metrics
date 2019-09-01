import socket
import os

udp_ip = "127.0.0.1"
udp_port = 4004

#udp_ip_send = "127.0.0.1"
udp_port_send = 3003

sockS = socket.socket(socket.AF_INET, # Internet
                    socket.SOCK_DGRAM) # UDP
					
sockC = socket.socket(socket.AF_INET, # Internet
                    socket.SOCK_DGRAM) # UDP
                     
# Faz o bind local. Associa um socket com um IP e uma Porta.
sockS.bind((udp_ip, udp_port))

while True:
	message, addr = sockS.recvfrom(1024) # Tamanho do buffer eh 1024 bytes
	print message
	sockC.sendto(message + " foi recebida", (addr[0], udp_port_send)) # Resposta do server para calcular latencia (RTT)

sockC.close()
sockS.close()

