#Implemente um método que identifique se uma árvore binária é simétrica. Uma árvore é simétrica se a subárvore esquerda for um espelho da subárvore direita.

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

RAIZ="raiz"

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

    # noSubEsquerda navegará na sub arvore da esquerda, enquanto o noSubDireita navegará na sub arvore da direita
    def simetrica(self, lista_aux: List, noSubEsquerda: 'No' = RAIZ, noSubDireita: 'No' = RAIZ):
        if noSubEsquerda is RAIZ and noSubDireita is RAIZ:
            noSubEsquerda = self.raiz
            noSubDireita = self.raiz
        
        
        # Enquanto a sub árvore a esquerda tenha elementos a esquerda, a sub árvore a direita deverá ter elementos a direita
        if noSubEsquerda.esquerda:
            if noSubDireita.direita:
                self.simetrica(lista_aux, noSubEsquerda.esquerda, noSubDireita.direita)
            # Caso contrário será incluso na lista_aux
            else:
                lista_aux.append("Não simétrico")        
        
        
        # Enquanto a sub árvore a direita tenha elementos a direita, a sub árvore a esquerda deverá ter elementos a esquerda
        if noSubEsquerda.direita:
            if noSubDireita.esquerda:
                self.simetrica(lista_aux, noSubEsquerda.direita, noSubDireita.esquerda)
            # Caso contrário será incluso na lista_aux
            else:
                lista_aux.append("Não simétrico")

'''''     
# Desenho da arvore 1                                  # Desenho da árvore 2           

                         30                                                        30                                          
                       /    \                                                    /    \          
                     20      40                                                20      40       
                   /   \    /   \                                             /   \   /   \             
                  10   25  35    50                                          10   25 35    50          
                 /              /  \
                5              45   55                                    

'''''


if __name__ == '__main__':
    arvore1 = Arvore_de_busca(No(30))
    arvore1.inserir(No(20))
    arvore1.inserir(No(40))
    arvore1.inserir(No(10))
    arvore1.inserir(No(25))
    arvore1.inserir(No(35))
    arvore1.inserir(No(5))
    arvore1.inserir(No(50))
    arvore1.inserir(No(55))
    arvore1.inserir(No(45))


    lista_aux_arvore1 = []
    arvore1.simetrica(lista_aux = lista_aux_arvore1)
    
    # Caso a lista_aux_arvore1 seja vazia a arvore é simétrica, caso contrário não
    if len(lista_aux_arvore1) == 0:
        print("Árvore 1 Simétrica")
    else:
        print("Árvore 1 não simétrica")    


    arvore2 = Arvore_de_busca(No(30))
    arvore2.inserir(No(20))
    arvore2.inserir(No(40))
    arvore2.inserir(No(10))
    arvore2.inserir(No(25))
    arvore2.inserir(No(35))
    arvore2.inserir(No(50))

    lista_aux_arvore2 = []
    arvore2.simetrica(lista_aux = lista_aux_arvore2)
    
    # Caso a lista_aux_arvore2 seja vazia a arvore é simétrica, caso contrário não
    if len(lista_aux_arvore2) == 0:
        print("Árvore 2 Simétrica")
    else:
        print("Árvore 2 não simétrica") 

