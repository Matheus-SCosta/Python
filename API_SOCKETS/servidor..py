#!/usr/bin/python3
import os
import socket
import subprocess

HOST = ''
PORT = 40000
TAM_MSG = 7000
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv = (HOST, PORT)
sock.bind(serv)
sock.listen(50)

def load():
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
                    domain = ''.join(msg[2:])
                    local_ip_address = '127.0.0.1'
                    if msg[1].lower() == '-p':
                        active_connections = ActiveConnections()
                        name_server, operational_system, ip_server_address = DataServer()
                        data_to_transfer = name_server + " " + operational_system + " " + ip_server_address + active_connections
                        # Mensagem enviada ao cliente
                        con.send(str.encode(data_to_transfer))
                
                
                    elif msg[1].lower() == '-c': 
                        data_to_transfer, data_to_http = TestingConnectivity(domain)
                        name_server, operational_system, ip_server_address = DataServer()
                        data_to_transfer = name_server + " " + operational_system + " " + ip_server_address + data_to_transfer + data_to_http
                        # Mensagem enviada ao cliente
                        print(data_to_transfer)
                        con.send(str.encode(data_to_transfer)) 

                
                    elif msg[1].lower() == '-a':
                        # Utilizando da biblioteca subprocess para verificar as portas abertas no servidor
                        open_doors = OpenDoors(local_ip_address)
                        name_server, operational_system, ip_server_address = DataServer()
                        data_to_transfer = name_server + " " + operational_system + " " + ip_server_address + open_doors
                        # Mensagem enviada ao cliente
                        con.send(str.encode(data_to_transfer))
                
                
                    else:
                        con.send(str.encode('Invalid Command'))
                        
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


def DataServer():
    # Utilizando da biblioteca os para verificar informações de nome e sistema operacional do servidor, e utilizando a biblioteca subprocess para verificar informações do endereçamento IP do servidor
    server_data = os.uname()
    name_server = server_data.nodename
    operational_system = server_data.sysname
    ip_server_address = subprocess.run(['hostname', '-I'], stdout=subprocess.PIPE)
    ip_server_address = ip_server_address.stdout.decode('utf-8')
    return name_server, operational_system, ip_server_address


def ActiveConnections():
     # Utilizando da biblioteca subprocess para fazer verificar as conexões estabelecidas do servidor
    active_connections = subprocess.run(['netstat','-nt'], stdout=subprocess.PIPE)
    active_connections = active_connections.stdout.decode('utf-8')
    return active_connections


def TestingConnectivity(domain):
    # Usando utilitário de dns para tradução de endereço IP
    dns = subprocess.run(['host', domain], stdout=subprocess.PIPE) 
    dns = dns.stdout.decode('utf-8')
    dns = dns.split()
    # Encontrar endereço ip do servidor
    for i in range(len(dns)): 
        if dns[i] == "address":
            domain_ip_address = dns[i+1]
            break
                       
    # Utilizando da biblioteca subprocess para fazer o teste de conexão e fazendo teste de conectividade com o utilitário de icmp com o endereço ip do dns passado como argumento
    testing_connectivity = subprocess.run(['ping','-c', '4', domain_ip_address], stdout=subprocess.PIPE) 
    testing_connectivity = testing_connectivity.stdout.decode('utf-8')
    testing_connectivity = testing_connectivity.split()
    # Verificando se há pacotes recebidos do ping, caso tenha significa que o servidor local tem conexões externas
                    
    if int(testing_connectivity[47]) > 0:  
        status = "Server with external connection"
        # Caso tenha conexão, será mostrado campos do cabeçalho http (presente em todos os dominios) usando o protocolo HTTP.
        http_connection = subprocess.run(['http','-h', 'http://'+domain], stdout=subprocess.PIPE) 
        http_connection = http_connection.stdout.decode('utf-8')
        http_connection = http_connection.split('\n')
        header_http=[]
        for linha in http_connection:
            linha = linha.split()
            if linha[0] == 'Connection:' or  linha[0] == 'HTTP/1.1' or linha[0] == 'Location:' or linha[0] == 'Location:':
                print(linha[0], linha[1])
                header_http.append(linha[0])
                header_http.append(linha[1])
                if linha[0] == 'Location:':
                    break
    else:
        status = "Server without external connection"
    # Mensagem que será enviada para o cliente sendo guardada em uma variável    
    data_to_transfer = '{} packets transmitted and {} packets received. {} to DNS {}'.format(testing_connectivity[44], testing_connectivity[47], status, domain)
    data_to_http = '\nHttp header details: \n{} {}\n{} {}\n{} {}'.format(header_http[0], header_http[1], header_http[2], header_http[3], header_http[4], header_http[5])
    return data_to_transfer, data_to_http


def OpenDoors(local_ip_address):
    # Utilizando da biblioteca subprocess para verificar as portas abertas no servidor
    open_doors = subprocess.run(['nmap', local_ip_address], stdout=subprocess.PIPE)
    open_doors = open_doors.stdout.decode('utf-8')
    return open_doors

load()        
