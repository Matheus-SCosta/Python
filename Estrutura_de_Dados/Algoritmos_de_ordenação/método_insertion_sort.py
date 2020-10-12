from typing import List
import csv


servidores_dns = []
with open('servidores_dns_br.csv') as csv_file:
  csv_reader = csv.reader(csv_file, delimiter=';')
  next(csv_reader, None)                                      # pula os cabeçalhos
  for row in csv_reader:
    servidor_dns = dict()
    servidor_dns['ip'] = row[0]
    servidor_dns['nome'] = row[1]
    servidores_dns.append(servidor_dns)

def insertion_sort_seq(lista: List):
    for i in range(1, len(lista)):                            # Começa do 2º elemento
        chave = lista[i]                                      # a variável chave recebe, as chaves ip e nome da biblioteca
        j = i - 1                                             # a variável j recebe o elemento anterior
        while j >= 0 and chave['nome'] < lista[j]['nome']:    # condição para entrar no laço precisa ser que j seja maior ou igual a 0 e caso o vetor esteja desordenado
            lista[j+1] = lista[j]                             # mudança de valores nas posições, para "abrir" espaço para a chave
            j -= 1                                            # A cada vez, diminui o valor de j, para fazer a comparação com os valores anteriores
        lista[j+1] = chave                                    # Ao não encontrar mais valores menores, e achar o local ordenado para o valor lista[i], a variável lista[j+1, recebe o valor guardado na variável chave
    return lista


print(insertion_sort_seq(servidores_dns))
