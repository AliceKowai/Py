class No:
    def __init__(self, chave, valor):
        self.chave = chave
        self.valor = valor
        self.proximo = None

class FilaEncadeada:
    def __init__(self, inicio=None):
        self.inicio = inicio
        self.final = inicio

    maxFila = 10
    fila = [None] * maxFila
    inicioFila = None
    finalFila = None

    def insere(self, novoNo):
        if self.inicio == None:  # fila vazia
            self.inicio = novoNo  # atualiza o início da fila
            self.final = novoNo  # atualiza o final da fila
        else:
            self.final.proximo = novoNo  # insere o nó
            self.final = novoNo  # atualiza o final da fila

    @staticmethod
    def insereFila(novoNo):
        global inicioFila  # indica o acesso a variáveis globais
        global maxFila
        global finalFila
        global fila
        if inicioFila is None:  # fila vazia
            fila[0] = novoNo  # insere o nó
            inicioFila = 0  # atualiza o início da fila
            finalFila = 0  # atualiza o final da fila
        elif (finalFila + 1) % maxFila == inicioFila:  # fila cheia
            return -1  # -1 indica erro de fila cheia
        else:
            finalFila = (finalFila + 1) % maxFila  # atualiza o final da fila
            fila[finalFila] = novoNo  # insere o nó
            return finalFila

    # remover

    def remove(self):
        if self.inicio == None:  # erro - fila vazia
            return None  # None indica erro fila vazia
        else:
            k = self.inicio  # salva o nó removido
            self.inicio = self.inicio.proximo  # remove o nó
            return k

    @staticmethod
    def removeFila():
        global inicioFila  # indica o acesso a variáveis globais
        global maxFila
        global finalFila
        global fila
        if inicioFila == None:  # fila vazia
            return None  # erro fila vazia
        k = fila[inicioFila]  # salva o nó removido
        if finalFila == inicioFila:
            inicioFila = None  # fila vazia após remoção
        else:
            inicioFila = (inicioFila + 1) % maxFila  # remove o nó
        return k  # retorne k = o nó consumido

    def busca(self, chave):
        noAtual = self.inicio
        while noAtual is not None:
            if noAtual.chave == chave:
                return noAtual
            noAtual = noAtual.proximo
        return None
    def print(self):
        elementos = []
        no_atual = self.inicio
        while no_atual:
            elementos.append((no_atual.chave, no_atual.valor))
            no_atual = no_atual.proximo
        print(elementos)

e0 = No(0, 'Joao')
fila = FilaEncadeada(e0)
k0 = fila.busca(0)
print(k0.valor)
fila.print()
e1 = No(1, 'Maria')
fila.insere(e1)
fila.print()
e2 = No(-1, 'Ana')
fila.insere(e2)
fila.print()
e3 = No(2, 'Arthur')
fila.insere(e3)
fila.print()
k = fila.remove()
print("No removido: " + k.valor)
fila.print()
