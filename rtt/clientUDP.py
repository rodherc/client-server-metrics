import socket
import os
import time
udp_ip = "127.0.0.1"
udp_port = 3032

udp_ip_send = "127.0.0.1"
udp_port_send = 3030

sock = socket.socket(socket.AF_INET, # Internet 
				 	socket.SOCK_DGRAM) # UDP

# Faz o bind local. Associa um socket com um IP e uma Porta.
sock.bind((udp_ip, udp_port))

while True:
	sendMessage = raw_input("Digite Sua Mensagem: ")
	
	if (sendMessage == "tchau"): # Encerra o programa
		exit()
	
	start = time.time() # Momento em que a mensagem e enviada
	sock.sendto(sendMessage, (udp_ip_send, udp_port_send))
	recvMessage, addr = sock.recvfrom(1024) # Tamanho do buffer eh 1024 bytes
	end = time.time()   # Momento em que a resposta do server e recebida
	
	print "Mensagem recebida: ", recvMessage
	print "Latencia (RTT): ", round(((end - start) * 1000), 4), "ms"

sock.close()	