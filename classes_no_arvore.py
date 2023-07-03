class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

    def insereEsquerda(self, valor):
        noEsquerda = No(valor)
        self.esquerda = noEsquerda

    def insereDireita(self, valor):
        noDireita = No(valor)
        self.direita = noDireita


class Arvore:

    def __init__(self, raiz):
        self.raiz = raiz

    def getValorRaiz(self):
        return self.valor

    def setValorRaiz(self, valor):
        self.valor = valor

    def insereNovoNo(self, noPai, valor):
        if valor < noPai.valor:
            if noPai.esquerda is None:
                novoNo = No(valor)
                noPai.esquerda = novoNo
            else:
                self.insereNovoNo(noPai.esquerda, valor)
        else:
            if noPai.direita is None:
                novoNo = No(valor)
                noPai.direita = novoNo
            else:
                self.insereNovoNo(noPai.direita, valor)

    def printPreorder(self, noPai):
        print(noPai.valor)
        if noPai.esquerda != None:
            self.printPreorder(noPai.esquerda)
        if noPai.direita != None:
            self.printPreorder(noPai.direita)

    def printPostorder(self, noPai):
        if noPai.esquerda != None:
            self.printPostorder(noPai.esquerda)
        if noPai.direita != None:
            self.printPostorder(noPai.direita)
        print(noPai.valor)

    def printInorder(self, noPai):
        if noPai.esquerda != None:
            self.printInorder(noPai.esquerda)
        print(noPai.valor)
        if noPai.direita != None:
            self.printInorder(noPai.direita)

    def imprimir_arvore(self, no, prefixo="", is_ultimo=True):
        # Imprime o prefixo
        print(prefixo, end="")

        # Verifica se é o último nó do nível
        if is_ultimo:
            print("`-- ", end="")
            prefixo += "    "
        else:
            print("|-- ", end="")
            prefixo += "|   "

        # Imprime o valor do nó atual
        print(no.valor)

        # Imprime os filhos recursivamente
        if no.direita != None:
            self.imprimir_arvore(no.direita, prefixo, no.direita.direita != None or no.direita.esquerda != None)

        if no.esquerda != None:
            self.imprimir_arvore(no.esquerda, prefixo, no.esquerda.direita != None or no.esquerda.esquerda != None)

    # - função que conte o número total de nós
    def contaNos(self, noPai):
        contador = 1
        if noPai.esquerda != None:
            contador += self.contaNos(noPai.esquerda)

        if noPai.direita != None:
            contador += self.contaNos(noPai.direita)

        return contador

    # - função que calcule a altura da árvore
    def getAltura(self, noPai):
        maiorAlturaFilhos = 0

        if noPai.esquerda != None:
            alturaFilhoEsquerda = self.contaNos(noPai.esquerda)

        if noPai.direita != None:
            alturaFilhoDireita = self.contaNos(noPai.direita)

        if alturaFilhoEsquerda > maiorAlturaFilhos:
            maiorAlturaFilhos = alturaFilhoEsquerda

        if alturaFilhoDireita > maiorAlturaFilhos:
            maiorAlturaFilhos = alturaFilhoDireita

        return 1 + maiorAlturaFilhos

    # - função que calcule o número de folhas
    def getFolhas(self, noPai):

        if noPai.direita == None and noPai.esquerda == None:
            return 1
        else:
            nosFolhas = 0
            if noPai.esquerda != None:
                nosFolhas += self.getFolhas(noPai.esquerda)

            if noPai.direita != None:
                nosFolhas += self.getFolhas(noPai.direita)

            return nosFolhas

