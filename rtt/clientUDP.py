import socket
import os
import time
udp_ip = "192.168.1.8"
udp_port = 3032

udp_ip_send = "192.168.1.5"
udp_port_send = 4444

sock = socket.socket(socket.AF_INET, # Internet 
				 	socket.SOCK_DGRAM) # UDP

# Faz o bind local. Associa um socket com um IP e uma Porta.
sock.bind((udp_ip, udp_port))
rtt = 0
for i in range(20):
	sendMessage = "Mensagem " + str(i) + " enviada\n"	
	start = time.time() # Momento em que a mensagem e enviada
	sock.sendto(sendMessage, (udp_ip_send, udp_port_send))
	recvMessage, addr = sock.recvfrom(1024) # Tamanho do buffer eh 1024 bytes
	end = time.time()   # Momento em que a resposta do server e recebida
	rtt += round(((end - start) * 1000), 4)

print "Latencia (RTT) medio: ",rtt/20 , "ms"

sock.close()	