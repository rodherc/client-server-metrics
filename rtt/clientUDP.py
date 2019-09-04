import socket
import os
import time

def to_miliseconds(seconds): # Transforma segundos em milisegundos
	return round(seconds * 1000,4) # Arredondamento com 4 casas

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
num_pacotes_total = 20
num_pacotes_perdidos = 0

for i in range(num_pacotes_total):
	send_message = "Mensagem " + str(i)	
	start = time.time() # Momento em que a mensagem e enviada
	sock.sendto(send_message, (udp_ip_send, udp_port_send))
	
	try:
		recv_message, addr = sock.recvfrom(1024) # Tamanho do buffer eh 1024 bytes
	except socket.timeout: # Nao recebeu a resposta no tempo limite
		num_pacotes_perdidos += 1
		print "Timeout\n"
		#time.sleep(1)
		continue
	
	end = time.time()   # Momento em que a resposta do server e recebida
	
	if (recv_message != ''):
		rtt = end - start
		soma_rtt += rtt
		print recv_message + ", ping: " + str(to_miliseconds(rtt)) + " ms" 
	#time.sleep(1)

num_pacotes_enviados = num_pacotes_total - num_pacotes_perdidos
rtt_medio = soma_rtt/num_pacotes_enviados

print "Latencia (RTT) medio: "+ str(to_miliseconds(rtt_medio)) + " ms"
print "Vazao: " + str( round(len(send_message.encode("utf8")) / (rtt_medio * 1000))) + " kb/s"
print str(num_pacotes_perdidos) + " pacotes perdidos"
sock.close()
