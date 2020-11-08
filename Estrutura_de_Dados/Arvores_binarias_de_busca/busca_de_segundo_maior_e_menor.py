# Desenvolva um método que determine o segundo menor elemento e o segundo maior elemento em uma árvore binária de busca.

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

    def buscar(self, no='No', raiz=RAIZ):
        if raiz == RAIZ:
            raiz = self.raiz
        if no.carga == raiz.carga:
            return "Encontrado"
        if no.carga > raiz.carga:
            if raiz.direita is None:
                return "Não encontrado"
            return self.buscar(no, raiz.direita)
        if no.carga < raiz.carga:
            if raiz.esquerda is None:
                return "Não encontrado"
            return self.buscar(no, raiz.esquerda)

    def segundo_maior_menor(self, raiz=RAIZ):
        if raiz == RAIZ:
            raiz = self.raiz
        
	# Enquanto houver elementos a esquerda a raiz é atribuido a variável segundo_menor
        while raiz.esquerda:
            segundo_menor = raiz
            raiz = raiz.esquerda
        
	# Voltando para raiz da árvore para buscar o segundo maior elemento
        raiz = self.raiz
        
	# Enquanto houver elementos a direita a raiz é atribuido a variável segundo_maior
        while raiz.direita:
            segundo_maior = raiz
            raiz = raiz.direita
        print(f"Segundo menor sem recursão: {segundo_menor} \nSegundo maior sem recursão: {segundo_maior}")

    def segundo_menor(self, no_anterior=None, raiz=RAIZ):
        if raiz == RAIZ:
            raiz = self.raiz
        if raiz.esquerda is not None:
            no_anterior = raiz
            return self.segundo_menor(no_anterior, raiz.esquerda)
        return no_anterior

    def segundo_maior(self, no_anterior=None,raiz=RAIZ):
        if raiz == RAIZ:
            raiz = self.raiz
        if raiz.direita is not None:
            no_anterior = raiz
            return self.segundo_maior(no_anterior, raiz.direita)
        return no_anterior



if __name__ == '__main__':
    arvore = Arvore_de_busca(No(30))
    arvore.inserir(No(20))
    arvore.inserir(No(15))
    arvore.inserir(No(10))
    arvore.inserir(No(40))
    arvore.inserir(No(45))
    arvore.inserir(No(50))
    # segundo maior e menor sem recursão
    arvore.segundo_maior_menor()

    # segundo maior e menor com recursão
    segundoMaior = arvore.segundo_maior()
    segundoMenor = arvore.segundo_menor()
    print("Segundo menor recursivo: ",segundoMenor)
    print("Segundo maior recursivo: ",segundoMaior)

