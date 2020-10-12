from typing import List
import csv


servidores_dns = []
with open('servidores_dns_br.csv') as csv_file:
  csv_reader = csv.reader(csv_file, delimiter=';')
  next(csv_reader, None)                        # pula os cabeçalhos
  for row in csv_reader:
    servidor_dns = dict()
    servidor_dns['ip'] = row[0]
    servidor_dns['nome'] = row[1]
    servidores_dns.append(servidor_dns)

def selection_sort_alg(vetor: List[dict]):
    for i in range(len(vetor)):                 # guarda a posição "menor", "inicial", cujo será colocado o menor valor, encontrado no proximo for
        aux = vetor[i]                          # guarda o valor da biblioteca na posição i 'ip' e 'nome', para a troca no final do programa
        menor = vetor[i]['nome']                # guarda o valor 'nome' da posição i, cujo inicialmente será o menor
        posicao_menor = i                       # guarda a posição de i, cujo inicialmente será o menor
        for k in range(i+1, len(vetor)):        # Varre o vetor por completo em busca do menor valor a partir do valor posterior a i, pois o i já foi lido no for anterior
            if vetor[k]['nome'] < menor:        # Compara o valor atual 'nome' da biblioteca, com o valor guardado na variável menor, atribuido no for anterior
                aux = vetor[k]                  # sendo menor, substitui 'ip' e 'nome' da posição k da biblioteca na variável aux
                menor = vetor[k]['nome']        # sendo menor, substitui o valor 'nome' da posição k da biblioteca na variável menor
                posicao_menor = k               # sendo menor, substitui a posição k na variável posição menor
        vetor[posicao_menor] = vetor[i]         # Nessa linha e na de baixo é a da troca, cujo a posição k, será o valor que tem na posição i
        vetor[i] = aux                          # E o vetor da posição i, vai receber o valor que está na variável aux, cujo tem o valor de k
    return vetor

print(selection_sort_alg(servidores_dns)) 
