#!/usr/bin/python3
import os
import socket
import subprocess

HOST = ''
PORT = 40000
TAM_MSG = 3000
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv = (HOST, PORT)
sock.bind(serv)
sock.listen(50)
while True:
    try:
        con, cliente = sock.accept()
    except: break
    pid = os.fork()
    if pid == 0:
        print('Cliente conectado', cliente)
        while True:
            msg = con.recv(TAM_MSG)
            if not msg: break
            msg = msg.decode().split()
            print(msg)
            if msg[0].lower() == 'connection':
                endereco = ''.join(msg[2:])
                enderecolocal = '127.0.0.1'

                
                if msg[1].lower() == '-p':
                    # Utilizando da biblioteca subprocess para fazer verificar as conexões estabelecidas do servidor
                    netstat = subprocess.run(['netstat','-nt'], stdout=subprocess.PIPE)
                    comando_netstat = netstat.stdout.decode('utf-8')
                    # Encaminhando mensagem ao cliente
                    con.send(str.encode(comando_netstat))
                
                
                elif msg[1].lower() == '-c':
                    # Usando utilitário de dns para tradução de endereço IP
                    dns = subprocess.run(['host', endereco], stdout=subprocess.PIPE) 
                    comando_dns = dns.stdout.decode('utf-8')
                    comando_dns = comando_dns.split()
                    # Encontrar endereço ip do servidor
                    for i in range(len(comando_dns)): 
                        if comando_dns[i] == "address":
                            endereco_ip = comando_dns[i+1]
                            break
                    # Utilizando da biblioteca subprocess para fazer o teste de conexão        
                    ping = subprocess.run(['ping','-c', '4', endereco_ip], stdout=subprocess.PIPE) 
                    # Fazendo teste de conectividade com o utilitário de icmp com o endereço ip do dns passado como argumento
                    comando_ping = ping.stdout.decode('utf-8')
                    divisao_ping = comando_ping.split()
                    # Verificando se há pacotes recebidos do ping, caso tenha significa que o servidor local tem conexões externas
                    if int(divisao_ping[48]) > 0:  
                        status = "Server with external connection"
                    else:
                        status = "Server without external connection"
                    # Mensagem que será enviada para o cliente sendo guardada em uma variável    
                    msg_ping = str.encode('{} packets transmitted and {} packets received. {} to {}'.format(divisao_ping[45], divisao_ping[48], status, endereco))
                    # Mensagem enviada ao cliente
                    con.send(msg_ping) 

                
                elif msg[1].lower() == '-a':
                    # Utilizando da biblioteca subprocess para verificar as portas abertas no servidor
                    nmap = subprocess.run(['nmap', enderecolocal], stdout=subprocess.PIPE)
                    comando_nmap = nmap.stdout.decode('utf-8')
                    # Mensagem enviada ao cliente
                    con.send(str.encode(comando_nmap))
                
                
                else:
                    endereco = ''.join(msg[1:])
                    dns = subprocess.run(['host', endereco], stdout=subprocess.PIPE) # Usando utilitário de dns para tradução de endereço IP
                    comando_dns = dns.stdout.decode('utf-8')
                    comando_dns = comando_dns.split()
                    for i in range(len(comando_dns)): # Encontrar endereço ip do servidor
                        if comando_dns[i] == "address":
                            endereco_ip = comando_dns[i+1]
                            break
                    ping = subprocess.run(['ping','-c', '4', endereco_ip], stdout=subprocess.PIPE)
                    netstat = subprocess.run(['netstat','-nt'], stdout=subprocess.PIPE)
                    nmap = subprocess.run(['nmap', enderecolocal], stdout=subprocess.PIPE)
                    comando_netstat = netstat.stdout.decode('utf-8')                        
                    comando_ping = ping.stdout.decode('utf-8')
                    comando_nmap = nmap.stdout.decode('utf-8')
                    todos = comando_nmap + comando_ping + comando_netstat + endereco
                    con.send(str.encode(todos))
                        
            # QUIT
            elif msg[0].lower() == 'quit':
                break
            else:
                con.send(str.encode('Invalid Command'))

        print('Cliente desconectado', cliente)
        con.close()
        break
    else:
        con.close()
sock.close()

