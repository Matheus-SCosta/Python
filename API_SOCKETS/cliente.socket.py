#!/usr/bin/env python3
import socket
import sys

TAM_MSG = 3000
HOST = '192.168.0.10'
PORT = 40000

if len(sys.argv) > 1:
    HOST = sys.argv[1]

serv = (HOST, PORT)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect (serv)

while True:
	try:
		cmd = input('CONNECTION-> ')
	except:
		cmd = 'QUIT'
		break

	sock.send(str.encode(cmd))
	dados = sock.recv(TAM_MSG)

	if not dados: break

	cmd = cmd.split()

	
	if cmd[0].lower() == 'connection': 
		# Caso a opção enviada pelo cliente seja -p, cujo mostrará de forma organizada as conexões ativas no servidor, seguindo o modelo IP:PORTA
		# Sintaxe do comando: connection -p
		if cmd[1].lower() == '-p':
			message = dados.decode().split()
			print("-----------------------------------------------------")
			print("\nServer data:\n")
			print("Name Server: ", message[0])
			print("Operational_system: ", message[1])
			print("IP private: ", message[2])
			print("\n-----------------------------------------------------")
			print("\nConnections established on the server\n")
			for i in range(len(message)):
				if str(message[i]) == "ESTABELECIDA":
					print(message[i-1])	
			print("\n")
		# Caso a opção enviada pelo cliente seja -c, cujo mostrará de forma organizada se o servidor tem conexão externa com algum DNS passado como argumento da opção -c.
		# Sintaxe do comando: connection -c ['URL']
		elif cmd[1].lower() == '-c':
			message = dados.decode().split('\n')
			message_aux = dados.decode().split()
			print("-----------------------------------------------------")
			print("\nServer data:\n")
			print("Name Server: ", message_aux[0])
			print("Operational_system: ", message_aux[1])
			print("IP private: ", message_aux[2])
			print("\n-----------------------------------------------------")
			print("\nTesting external server connection\n")
			print(message[1])
			print("\n")

		# Caso a opção enviada pelo cliente seja -a, cujo mostrará de forma organizada as portas abertas do servidor seguindo o modelo # PORT: porta/protocolo_camada_de_transporte
		# Sintaxe do comando: connection -a                                                                                            # STATE: status da porta (aberta)
		elif cmd[1].lower() == '-a':                                                                                                   # SERVICE: Serviço que está rodando na porta 
			message = dados.decode().split()
			print("-----------------------------------------------------")
			print("\nServer data:\n")
			print("Name Server: ", message[0])
			print("Operational_system: ", message[1])
			print("IP private: ", message[2])
			print("\n-----------------------------------------------------")
			print("\nOpen ports on server:\n")                                                                                         
			counter = 0
			# Organização dos dados recebidos pelo servidor, cujo mostrará de forma organizada as portas abertas do servidor
			while message[counter] != "seconds":
				if str(message[counter]) == "SERVICE":
					counter = counter + 1
					auxiliary_accountant = 0
					auxiliary_accountant2 = 1	
					while message[counter] != "Nmap":
						if auxiliary_accountant == 3:
							print("\n")
							auxiliary_accountant = 0
						if auxiliary_accountant2 == 1:
							print("PORT: ", message[counter])    # Exibindo o número da porta e protocolo
						elif auxiliary_accountant2 == 2:
							print("STATE: ", message[counter])   # Exibindo o status como aberta
						elif auxiliary_accountant2 == 3:
							print("SERVICE: ", message[counter])  # Exibindo qual o serviço que está disponível na porta
							auxiliary_accountant2 = 0		
						counter = counter + 1
						auxiliary_accountant = auxiliary_accountant + 1
						auxiliary_accountant2 = auxiliary_accountant2 + 1
				counter = counter + 1
			print("\n")
		# Caso o cliente não informe nenhuma opção, será exibido todas as informações. 
		# Sintaxe será: connection ['URL']
		else:
			message = dados.decode().split()
			counter = 0
			print("-----------------------------------------------------")
			print("\nServer data:\n")
			print("Name Server: ", message[0])
			print("Operational_system: ", message[1])
			print("IP private: ", message[2])
			print("\n-----------------------------------------------------")
			# mostrará de forma organizada as portas abertas do servidor seguindo o modelo # PORT: porta/protocolo_camada_de_transporte
			print("\nOpen ports on server:\n")                                             # STATE: status da porta (aberta)
			while message[counter] != "seconds":                                          # SERVICE: Serviço que está rodando na porta
				if str(message[counter]) == "SERVICE":
					counter = counter + 1
					auxiliary_accountant = 0
					auxiliary_accountant2 = 1	
					while message[counter] != "Nmap":
						if auxiliary_accountant == 3:
							auxiliary_accountant = 0
						if auxiliary_accountant2 == 1:
							print("PORT: ", message[counter])
						elif auxiliary_accountant2 == 2:
							print("STATE: ", message[counter])
						elif auxiliary_accountant2 == 3:
							print("SERVICE: ", message[counter])
							auxiliary_accountant2 = 0
							print("\n")		
						counter = counter + 1
						auxiliary_accountant = auxiliary_accountant + 1
						auxiliary_accountant2 = auxiliary_accountant2 + 1
				counter = counter + 1
			print("----------------------------------------------------")
			# mostrará de forma organizada se o servidor tem conexão externa com algum DNS passado como argumento.
			print("\nTesting external server connection:\n")
			ms = 0
			counter = counter + 1
			dns = len(message)
			while ms < 5:
				if message[counter] == "pacotes":
					print('{} packets transmitted and {} packets received. Server with external connection to DNS {}'.format(message[counter - 1], message[counter + 2], message[dns - 1]))
				if message[counter] == "ms":
					ms = ms + 1
				counter = counter + 1
			print("\n")
			# mostrará de forma organizada as conexões ativas no servidor, seguindo o modelo IP:PORTA		
			print("----------------------------------------------------")
			print("\nConnections established on the server (IP:PORT):\n")
			tamanho_total = len(message)			
			while counter < tamanho_total:
				if str(message[counter]) == "ESTABELECIDA":
					print(message[counter-1])
				counter = counter + 1
			print("\n")
	elif cmd[0].lower() == 'help':
		msg = ''.join(message[0])
		for linha in message:
			print(msg)
	
	elif cmd[0] == 'quit':
		msg = ''.join(message)
		print(msg)
		break
	
	else:
		msg = ''.join(message)
		print(f'-WRONG\n{msg}')
		print('Consulte "help"')

