import socket
import os
import time

#Dados server
UDP_IP_SEND = "192.168.103.8"
UDP_PORT_SEND = 4004

sock_udp = socket.socket(socket.AF_INET, # Internet 
				 	socket.SOCK_DGRAM) # UDP

sock_udp.settimeout(0.1)

sum_rtt = 0
num_pacotes_total = 20
num_pacotes_perdidos = 0

for i in range(num_pacotes_total):
	send_message = "Mensagem " + str(i)
	time.sleep(0.250)	
	start = time.time() # Momento em que a mensagem e enviada
	sock_udp.sendto(send_message, (UDP_IP_SEND, UDP_PORT_SEND))
	
	try:
		recv_message = sock_udp.recvfrom(1024) # Tamanho do buffer eh 1024 bytes
	except socket.timeout: # Nao recebeu a resposta no tempo limite
		num_pacotes_perdidos += 1
		#print "Timeout"
		continue
	
	end = time.time()   # Momento em que a resposta do server e recebida
	
	if (recv_message != ''):
		rtt = end - start
		sum_rtt += rtt
		#print "ping:", round(rtt * 1000,4), " ms" 

num_pacotes_enviados = num_pacotes_total - num_pacotes_perdidos
if num_pacotes_enviados != 0:
	rtt_medio = sum_rtt/num_pacotes_enviados
	print "Latencia (RTT) medio:", round(rtt_medio * 1000,4), "ms"
print num_pacotes_perdidos, "pacotes perdidos"
sock_udp.close()
