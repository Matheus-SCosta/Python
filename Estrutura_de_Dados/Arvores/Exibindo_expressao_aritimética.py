# Crie um método para navegar na árvore e exibir a expressão matemática. Neste caso, utilize o que você aprendeu sobre os métodos de navegação (pré-ordem, in-ordem ou pós-ordem) para exibir os 
# parênteses da esquerda, os parênteses da direita e o valor de cada nó.


class No:
    def __init__(self, carga, esquerda: 'No', direita: 'No'):
        self.carga = carga
        self.esquerda = esquerda
        self.direita = direita

    def __str__(self):
        return self.carga

class ArvoreBinaria:
    def __init__(self, raiz: 'No'):
        self.raiz = raiz

    def in_ordem(self, no: 'No' = None):
        if no is None:
            return no
        if no.esquerda:
            self.in_ordem(no.esquerda)
        print(no, end='')
        if no.direita:
            self.in_ordem(no.direita)

if __name__ == '__main__':
    no17 = No(")", None, None) 
    no16 = No(")", None, None)
    no15 = No(")", None, None) 
    no14 = No(")", None, None) 
    no13 = No("(", None, None)
    no12 = No("(", None, None) 
    no11 = No("(", None, None) 
    no10 = No("(", None, None)
    no9 = No("7", None, None)
    no8 = No("2", None, None)
    no7 = No("20", None, None)
    no6 = No("/", None, None)
    no5 = No("-", None, None)
    no4 = No("10", None, None)
    no3 = No("*", None, None)
    no2 = No("12", None, None)
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
    arvore.in_ordem(arvore.raiz)
