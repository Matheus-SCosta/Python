from typing import List
import csv


servidores_dns = []
with open('servidores_dns_br.csv') as csv_file:
  csv_reader = csv.reader(csv_file, delimiter=';')
  next(csv_reader, None)  				      # pula os cabeçalhos
  for row in csv_reader:
    servidor_dns = dict()
    servidor_dns['ip'] = row[0]
    servidor_dns['nome'] = row[1]
    servidores_dns.append(servidor_dns)


def bolha(vetor: List[dict]):
    trocou: bool = True
    while trocou:
        trocou = False
        for i in range(len(vetor)-1):
            if vetor[i]['nome'] > vetor[i+1]['nome']:         # Compara os valores da chave nome da biblioteca
                aux = vetor[i]                                # entrando na condição guarda-se o valor do vetor i, em uma variavel auxiliar
                vetor[i] = vetor[i+1]                         # a posição i, recebe a posição i+1, cujo é menor de que a posição i
                vetor[i+1] = aux                              # a posição i+1 recebe o valor guardado na variável auxiliar
                trocou = True
    return vetor

print(bolha(servidores_dns))
