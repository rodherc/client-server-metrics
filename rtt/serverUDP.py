import socket
import os

udp_ip = "127.0.0.1"
udp_port = 3030

udp_ip_send = "127.0.0.1"
udp_port_send = 3032

sock = socket.socket(socket.AF_INET, # Internet
                    socket.SOCK_DGRAM) # UDP
                     
# Faz o bind local. Associa um socket com um IP e uma Porta.
sock.bind((udp_ip, udp_port))

while True:
	message, addr = sock.recvfrom(1024) # Tamanho do buffer eh 1024 bytes
	print "Mensagem recebida:", message
	sock.sendto(message, (udp_ip_send, udp_port_send)) # Resposta do server para calcular latencia (RTT)

sock.close()

