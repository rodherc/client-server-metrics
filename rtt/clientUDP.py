import socket
import os
import time

udp_ip = "127.0.0.1"
udp_port = 3003

udp_ip_send = "127.0.0.1"
udp_port_send = 4004

sock = socket.socket(socket.AF_INET, # Internet 
				 	socket.SOCK_DGRAM) # UDP

sock.settimeout(0.1)

# Faz o bind local. Associa um socket com um IP e uma Porta.
sock.bind((udp_ip, udp_port))
soma_rtt = 0
num_pacotes_perdidos = 0

for i in range(20):
	sendMessage = "Mensagem " + str(i)	
	start = time.time() # Momento em que a mensagem e enviada
	sock.sendto(sendMessage, (udp_ip_send, udp_port_send))
	try:
		recvMessage, addr = sock.recvfrom(1024) # Tamanho do buffer eh 1024 bytes
	except socket.timeout: # Nao recebeu a resposta no tempo limite
		num_pacotes_perdidos += 1
		print "Timeout\n"
		#time.sleep(1)
		continue
	
	end = time.time()   # Momento em que a resposta do server e recebida
	
	if (recvMessage != ''):
		rtt = round(((end - start) * 1000), 4)
		soma_rtt += rtt
		print recvMessage + ", rtt: " + str(rtt) + "ms" 
	#time.sleep(1)

print "Latencia (RTT) medio: "+ str(soma_rtt/20) + "ms"
print str(num_pacotes_perdidos) + " numero de pacotes perdidos"
#print "Vazao:"
sock.close()	