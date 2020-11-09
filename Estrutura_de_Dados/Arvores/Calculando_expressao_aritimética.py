# Crie um método para calcular o valor resultante da expressão.

from typing import List

class No:
    def __init__(self, carga, esquerda: 'No', direita: 'No'):
        self.carga = carga
        self.esquerda = esquerda
        self.direita = direita

class ArvoreBinaria:
    def __init__(self, raiz: 'No'):
        self.raiz = raiz

    def calculo(self, lista):
        posicao_x = 0                    # guardará a posição do vetor do sinal de *
        condicao_x = False               # Será determinando para calculo, caso necessário seja alterada para True
        posicao_mais = 0
        condicao_mais = False
        posicao_divisao = 0
        condicao_divisao = False
        posicao_subtracao = 0
        condicao_subtracao = False
        tamanho_da_lista = len(lista)

        if tamanho_da_lista <= 1:                                                       # Condição de parada
            return lista[0]                                                             # Retorna o único elemento da lista, cujo é o resultado da expressão
        for i in range(tamanho_da_lista):
            if lista[i] == "(":                                                         # Entra na condição em alguma abertura de parênteses
                posicao_caractere = i                                                   # Guarda a posição do parênteses no vetor
                if type(lista[i + 1]) == int and type(lista[i + 3]) == int:             # Entra na condição, caso o primeiro e terceiro elemento após sua posição sejam inteiros
                    if lista[i + 2] == "*":                                             # Verifica qual sinal de operação tem 2 posições após o parênteses
                        posicao_x = i                                                   # Guarda a posição
                        condicao_x = True                                               # Muda para True caso encontre o sinal de operação *
                    if lista[i + 2] == "+":
                        posicao_mais = i
                        condicao_mais = True
                    if lista[i + 2] == "-":
                        posicao_subtracao = i
                        condicao_subtracao = True
                    if lista[i + 2] == "/":	
                        posicao_divisao = i
                        condicao_divisao = True
        if condicao_x:                                                                  # Se for True
            lista[posicao_x + 2] = lista[posicao_x + 1] * lista[posicao_x + 3]          # Altera o valor da posição onde tem o sinal *, para o calculo dos 2 inteiros, antes e depois do sinal. Ex: 10 * 8
            del (lista[posicao_x + 1])                                                  # Remove o elemento deste posição
            del (lista[posicao_x + 2])                                                  # Remove o elemento deste posição
            del (lista[posicao_caractere + 2])                                          # Remove o elemento da 2 posições a frente do "("
            del (lista[posicao_caractere])                                              # Remove o parêntese
            return self.calculo(lista)                                                  # Chama novamente a função com um dos calculos já feito
        if condicao_mais:
            lista[posicao_mais + 2] = lista[posicao_mais + 1] + lista[posicao_mais + 3]
            del (lista[posicao_mais + 1])
            del (lista[posicao_mais + 2])
            del (lista[posicao_caractere + 2])
            del (lista[posicao_caractere])
            return self.calculo(lista)
        if condicao_subtracao:
            lista[posicao_subtracao + 2] = lista[posicao_subtracao + 1] - lista[posicao_subtracao + 3]
            del (lista[posicao_subtracao + 1])
            del (lista[posicao_subtracao + 2])
            del (lista[posicao_caractere + 2])
            del (lista[posicao_caractere])
            return self.calculo(lista)
        if condicao_divisao:
            lista[posicao_divisao + 2] = lista[posicao_divisao + 1] // lista[posicao_divisao + 3]
            del (lista[posicao_divisao + 1])
            del (lista[posicao_divisao + 2])
            del (lista[posicao_caractere + 2])
            del (lista[posicao_caractere])
            return self.calculo(lista)

    def in_ordem(self, no: 'No' = None, lista=None):
        if no is None:
            return no
        if no.esquerda:
            self.in_ordem(no.esquerda, lista)
        lista.append(no.carga)
        if no.direita:
            self.in_ordem(no.direita, lista)

if __name__ == '__main__':
    no17 = No(")", None, None)
    no16 = No(")", None, None)
    no15 = No(")", None, None)w
    no14 = No(")", None, None)
    no13 = No("(", None, None)
    no12 = No("(", None, None)
    no11 = No("(", None, None)
    no10 = No("(", None, None)
    no9 = No(7, None, None)
    no8 = No(2, None, None)
    no7 = No(20, None, None)
    no6 = No("/", None, None)
    no5 = No("-", None, None)
    no4 = No(10, None, None)
    no3 = No("*", None, None)
    no2 = No(12, None, None)
    no1 = No("+", None, None)
    no1.esquerda = no2
    no1.direita = no3
    no2.esquerda = no10
    no3.esquerda = no4
    no3.direita = no5
    no4.esquerda = no11
    no5.esquerda = no6
    no5.direita = no9
    no6.esquerda = no7
    no6.direita = no8
    no7.esquerda = no12
    no8.direita = no14
    no12.esquerda = no13
    no9.direita = no15
    no15.esquerda = no16
    no16.esquerda = no17
    arvore = ArvoreBinaria(no1)
    listaaux = []
    arvore.in_ordem(arvore.raiz, listaaux)
    print("Calculo da expressão matemática: ",arvore.calculo(listaaux))
