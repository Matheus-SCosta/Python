# Crie um método para calcular a altura de uma árvore binária de busca



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


    def altura(self, no=RAIZ):
        if no == RAIZ:
            no = self.raiz
        alturaesquerda = 0
        alturadireita = 0
        if no.esquerda:
            alturaesquerda = self.altura(no.esquerda)
        if no.direita:
            alturadireita = self.altura(no.direita)
        if alturadireita > alturaesquerda:
            return alturadireita + 1
        return alturaesquerda + 1

'''''     
#Desenho da arvore: A                                              
                         30                           Altura 4                                        
                       /    \ 
                     20      40                       Altura 3                                                         
                   /   \       \ 
                  10   25      50                     Altura 2                                                 
                    \         /   \ 
                    15       37   800                 Altura 1
                                     \
                                    1264              Altura 0

'''''

if __name__ == '__main__':
    arvore = Arvore_de_busca(No(30))
    arvore.inserir(No(20))
    arvore.inserir(No(25))
    arvore.inserir(No(10))
    arvore.inserir(No(40))
    arvore.inserir(No(50))
    arvore.inserir(No(15))
    arvore.inserir(No(37))
    arvore.inserir(No(800))
    arvore.inserir(No(1264))
    altura = arvore.altura() - 1
    print("Altura da árvore: ", altura)

