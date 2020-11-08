# Construa um método para verificar se duas árvores binárias A e B são identicas

from typing import List


class No:
    def __init__(self, carga: object, esquerda: 'No' = None, direita: 'No' = None):
        self.carga = carga
        self.esquerda = esquerda
        self.direita = direita

    def __str__(self):
        return str(self.carga)


RAIZ = "raiz"


class ArvoreBinaria:
    def __init__(self, raiz: 'No'):
        self.raiz = raiz

    def em_ordem(self, no: 'No' = RAIZ):
        if no == RAIZ:
            no = self.raiz
        if no is None:
            return no
        if no.esquerda:
            self.em_ordem(no.esquerda)
        print(no, end=" ")
        if no.direita:
            self.em_ordem(no.direita)


RAIZ = "raiz"


class Arvore_de_busca(ArvoreBinaria):
    def inserir(self, no, raiz=RAIZ):
        if raiz == RAIZ:
            raiz = self.raiz
        if no.carga > raiz.carga:
            if raiz.direita == None:
                raiz.direita = no
            return self.inserir(no, raiz.direita)
        if no.carga < raiz.carga:
            if raiz.esquerda is None:
                raiz.esquerda = no
            return self.inserir(no, raiz.esquerda)

    def comparando_arvores(self, aux: List, noA, noB):
        if noA is None:
            return noA
        if noB is None:
            return noB

        # Compara se ambas as arvores tem elementos a esquerda - Caso a arvore A tenha e a arvore B não, é apresentado o erro e a inclusão de elemento na lista aux
        if noA.esquerda:
            if noB.esquerda:
                self.comparando_arvores(aux, noA.esquerda, noB.esquerda)
            else:  # se caso a arvore A tenha elementos a esquerda, e a arvore B não
                print("Arvores diferentes pois tem quantidade de elementos e/ou estruturas diferentes")
                aux.append("diferente")

        # Compara se ambas as arvores tem elementos a esquerda - Caso a arvore B tenha e a arvore A não, é apresentado o erro e a inclusão de elemento na lista aux
        if noB.esquerda:
            if noA.esquerda is None:
                print("Arvores diferentes pois tem quantidade de elementos e/ou estruturas diferentes")
                aux.append("diferente")

        #se um nó em mesma posição for diferente do outro
        if noA.carga != noB.carga:
            print("Arvores diferentes pois tem elementos diferentes")
            print(f"Em mesma posição na arvore A tem valor: {noA}")
            print(f"Enquanto a arvore B: {noB}")
            aux.append("diferente")

        # Compara se ambas as arvores tem elementos a direita - Caso a arvore B tenha e a arvore A não, é apresentado o erro e a inclusão de elemento na lista aux
        if noB.direita:
            if noA.direita is None:
                print("Arvores diferentes pois tem quantidade de elementos e/ou estruturas diferentes")
                aux.append("diferente")

        # Compara se ambas as arvores tem elementos a direita - Caso a arvore A tenha e a arvore A não, é apresentado o erro e a inclusão de elemento na lista aux
        if noA.direita:
            if noB.direita:
                self.comparando_arvores(aux, noA.direita, noB.direita)
            else:  # se caso a arvore A tenha elementos a direita, e a arvore B não
                print("Arvores diferentes pois tem quantidade de elementos e/ou estruturas diferentes")
                aux.append("diferente")


'''''     
#Desenho da arvore: A                                              #Desenho da arvore: B
                         30                                                                    30
                       /    \                                                                /    \
                     20      40                                                            20      40
                   /   \    /   \                                                        /   \    /   \
                  10   25  35    50                                                    15    25  35    50



'''''

if __name__ == '__main__':
    A = Arvore_de_busca(No(30))
    A.inserir(No(20))
    A.inserir(No(25))
    A.inserir(No(10))
    A.inserir(No(40))
    A.inserir(No(35))
    A.inserir(No(50))
    B = Arvore_de_busca(No(30))
    B.inserir(No(20))
    B.inserir(No(25))
    B.inserir(No(10))
    B.inserir(No(40))
    B.inserir(No(35))
    B.inserir(No(50))
    listaaux = []
    A.comparando_arvores(aux=listaaux, noA=A.raiz, noB=B.raiz)
    
    # Caso o vetor seja vazio é por que as arvores são iguais em valores dos nós e em estrutura
    if len(listaaux) == 0:
        print("Arvores são iguais")
