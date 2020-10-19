from statistics import median_low
from typing import List

class No:
    def __init__(self, carga, anterior=None, proximo=None):
        self.carga = carga
        self.anterior = anterior
        self.proximo = proximo


class Lista_Duplamente_Encadeada:
    def __init__(self, cabeca=None, cauda=None):
        self.cabeca = cabeca
        self.cauda = cauda

    def imprimir(self):
        if self.cabeca is None:
            print("Lista vazia")
            return
        atual = self.cabeca
        while atual:
            print(atual.carga)
            atual = atual.proximo

    def inserir_inicio(self, valor):
        valor: 'No' = No(valor)
        if self.cabeca is None:  
            self.cabeca = self.cauda = valor
            return
        valor.proximo = self.cabeca  
        self.cabeca.anterior = valor  
        self.cabeca = valor  



class Quicksort_Lista_Duplamente_Encadeada(Lista_Duplamente_Encadeada):
    def atualizar(self, carga: int, pos: int):
        posicao_lista = 0
        atual = self.cabeca
        while atual:
            if pos == posicao_lista:
                atual.carga = carga
                return
            posicao_lista = posicao_lista + 1
            atual = atual.proximo

    def quicksort(self, vetor: List):
        iguais = []
        menores = []
        maiores = []
        if len(vetor) <= 1:
            return vetor
        pivot = median_low(vetor)
        for i in range(len(vetor)):
            if vetor[i] == pivot:
                iguais.append(vetor[i])
        for i in range(len(vetor)):
            if vetor[i] < pivot:
                menores.append(vetor[i])
        for i in range(len(vetor)):
            if vetor[i] > pivot:
                maiores.append(vetor[i])
        return self.quicksort(menores) + iguais + self.quicksort(maiores)

    def ordenacao(self):
        vetor_desordenado = []
        atual = self.cabeca
        while atual:
            vetor_desordenado.append(atual.carga)
            atual = atual.proximo
        vetor_ordenado = self.quicksort(vetor_desordenado)
        for i in range(len(vetor_ordenado)):
            self.atualizar(vetor_ordenado[i], i)


def main():
    lista1 = Quicksort_Lista_Duplamente_Encadeada()
    lista1.inserir_inicio(5)
    lista1.inserir_inicio(1)
    lista1.inserir_inicio(9)
    lista1.inserir_inicio(6)
    lista1.inserir_inicio(0)
    lista1.inserir_inicio(2)
    lista1.inserir_inicio(17)
    lista1.inserir_inicio(60)
    lista1.inserir_inicio(56)
    lista1.inserir_inicio(25)
    print("Antes de ordenar:")
    lista1.imprimir()
    lista1.ordenacao()
    print("Depois de ordenar:")
    lista1.imprimir()

main()
