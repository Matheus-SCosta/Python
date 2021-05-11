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

	# Caso a opção enviada pelo cliente seja -p, cujo mostrará de forma organizada as conexões ativas no servidor, seguindo o modelo IP:PORTA
	# Sintaxe do comando: connection -a
	if cmd[0].lower() == 'connection': 
		if cmd[1].lower() == '-p':
			print("\nConnections established on the server\n")
			message = dados.decode().split()
			for i in range(len(message)):
				if str(message[i]) == "ESTABELECIDA":
					print(message[i-1])	
			print("\n")
		# Caso a opção enviada pelo cliente seja -c, cujo mostrará de forma organizada se o servidor tem conexão externa com algum DNS passado como argumento da opção -c.
		# Sintaxe do comando: connection -c ['URL']
		elif cmd[1].lower() == '-c':
			print("\nTesting external server connection\n")
			message = dados.decode().split('\n')
			for i in message:
				print(i)           # Exibido mensagem da forma que vem do servidor
			print("\n")

		# Caso a opção enviada pelo cliente seja -a, cujo mostrará de forma organizada as portas abertas do servidor seguindo o modelo # PORT: porta/protocolo_camada_de_transporte
		# Sintaxe do comando: connection -a                                                                                            # STATE: status da porta (aberta)
		elif cmd[1].lower() == '-a':                                                                                                   # SERVICE: Serviço que está rodando na porta 
			print("\nOpen ports on server:\n")                                                                                         
			message = dados.decode().split()
			contador = 0
			#Organização dos dados recebidos pelo servidor, cujo mostrará de forma organizada as portas abertas do servidor
			while message[contador] != "seconds":
				if str(message[contador]) == "SERVICE":
					contador = contador + 1
					contadoraux = 0
					contadoraux2 = 1	
					while message[contador] != "Nmap":
						if contadoraux == 3:
							print("\n")
							contadoraux = 0
						if contadoraux2 == 1:
							print("PORT: ", message[contador])    # Exibindo o número da porta e protocolo
						elif contadoraux2 == 2:
							print("STATE: ", message[contador])   # Exibindo o status como aberta
						elif contadoraux2 == 3:
							print("SERVICE: ", message[contador])  # Exibindo qual o serviço que está disponível na porta
							contadoraux2 = 0		
						contador = contador + 1
						contadoraux = contadoraux + 1
						contadoraux2 = contadoraux2 + 1
				contador = contador + 1
			print("\n")
		# Caso o cliente não informe nenhuma opção, será exibido todas as informações. 
		# Sintaxe será: connection ['URL']
		else:
			message = dados.decode().split()
			contador = 0
			print(message)
			# mostrará de forma organizada as portas abertas do servidor seguindo o modelo # PORT: porta/protocolo_camada_de_transporte
			print("\nOpen ports on server:\n")                                             # STATE: status da porta (aberta)
			while message[contador] != "seconds":                                          # SERVICE: Serviço que está rodando na porta
				if str(message[contador]) == "SERVICE":
					contador = contador + 1
					contadoraux = 0
					contadoraux2 = 1	
					while message[contador] != "Nmap":
						if contadoraux == 3:
							contadoraux = 0
						if contadoraux2 == 1:
							print("PORT: ", message[contador])
						elif contadoraux2 == 2:
							print("STATE: ", message[contador])
						elif contadoraux2 == 3:
							print("SERVICE: ", message[contador])
							contadoraux2 = 0
							print("\n")		
						contador = contador + 1
						contadoraux = contadoraux + 1
						contadoraux2 = contadoraux2 + 1
				contador = contador + 1

			print("\n")
			# mostrará de forma organizada se o servidor tem conexão externa com algum DNS passado como argumento.
			print("\nTesting external server connection:\n")
			ms = 0
			contador = contador + 1
			dns = len(message)
			while ms < 5:
				if message[contador] == "pacotes":
					print('{} packets transmitted and {} packets received. Server with external connection to {}'.format(message[contador - 1], message[contador + 2], message[dns - 1]))
				if message[contador] == "ms":
					ms = ms + 1
				contador = contador + 1
			print("\n")
			# mostrará de forma organizada as conexões ativas no servidor, seguindo o modelo IP:PORTA		
			print("\n")
			print("\nConnections established on the server:\n")
			tamanho_total = len(message)			
			while contador < tamanho_total:
				if str(message[contador]) == "ESTABELECIDA":
					print(message[contador-1])
				contador = contador + 1
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

