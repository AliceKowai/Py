from collections import deque


q=deque()			     #cria o deque
q.append('b')		     #insere no final
q.append('c')
q.appendleft('a')
print(q)			     #imprime o deque
print(q.popleft())	     #remove do inicio
print(q.pop())	

class No:
    def __init__(self, chave, valor):
        self.chave = chave
        self.valor = valor
        self.proximo = None
        self.anterior = None

class DequeEncadeada:
    def __init__(self, inicio=None):
        self.inicio = inicio
        self.final = inicio

maxDeque=10
deque=[None]*maxDeque
inicioDeque=None
finalDeque=None

def popBack(self):
    if self.inicio == None:  # erro - deque vazia
        return None  # None indica erro deque vazia
    else:
        k = self.final  # salva o nó removido
        self.final = self.final.anterior  # remove o nó
        self.final.proximo = None  # aponta o próximo do final para λ (vazio)
        return k
    

def popBack():
    global inicioDeque  # indica o acesso a variáveis globais
    global maxDeque
    global finalDeque
    global deque
    if inicioDeque == None:  # Deque vazia
        return None  # erro Deque vazia
    k = deque[inicioDeque]  # salva o nó removido
    if finalDeque == inicioDeque:
        inicioDeque = None  # Deque vazia após remoção
    else:
        finalDeque = (finalDeque - 1) % maxDeque  # remove o nó
    return k
	