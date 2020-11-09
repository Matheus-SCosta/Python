# Implemente um código python que represente a árvore binária contendo esses elementos. Crie as classes No, contendo os apontadores para os 
# elementos da esquerda e direita e a classe ArvoreBinaria contendo a referência para o elemento raiz


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


if __name__ == '__main__':
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
    no3.esquerda = no4
    no3.direita = no5
    no5.esquerda = no6
    no5.direita = no9
    no6.esquerda = no7
    no6.direita = no8
