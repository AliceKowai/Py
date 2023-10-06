# Listas, Pilhas, Filas e Deques

def trocar(seq, i):
    tmp = seq[i]
    seq[i] = seq[i+1]
    seq[i+1] = tmp


sequencia = [10, 5, 20, 1, 4]
troca = 1
while troca:
    troca = 0
    i = 0
    for i in range(0, len(sequencia)-1):
        if sequencia[i] > sequencia[i+1]:
            trocar(sequencia, i)
            troca = 1
print(sequencia)

#Lista sequenciais 

def buscaLista(k, L, n):
    i = 0
    índiceL = -1
    while i < n:
        if L[i] == k:  # nó encontrado
            indiceL = i  # salva o índice
            i = n+1  # sair do laço
        i = i+1  # segue a procura
    return indiceL


nomes = ['Arthur', 'Joao', 'Maria', 'Ana']
i = buscaLista('Ana', nomes, len(nomes))
print(i)
 
#Lista Ordenada

def buscaOrdenada(k, L, n):
    i = 0
    indiceL = -1
    while i < n:
        if L[i] >= k:
            if L[i] == k:
                indiceL = i  # chave encontrada
                i = n + 1    # sair do laço
            else:
                i = n + 1  # chave > k, sair do laço
        else:
            i = i + 1  # continuar busca
    return indiceL


numeros = [1, 2, 3, 4, 6, 7, 8, 9, 10]
i = buscaOrdenada(5, numeros, len(numeros))
print(i)
i = buscaOrdenada(3, numeros, len(numeros))
print(i)  # -1 indica chave não achada


def insereOrdenada(k, L, n):
    i = 0  # Inicializa um índice para buscar a posição de inserção.
    # Inicializa uma variável para armazenar a posição de inserção do novo elemento.
    posInsercao = -1

    while i < n:  # Inicia um loop que continuará enquanto o índice 'i' for menor que o número de elementos 'n' na lista.
        # Verifica se o elemento atual na posição 'i' da lista 'L' é maior ou igual ao valor 'k'.
        if L[i] >= k:
            # Se o elemento atual for igual a 'k', retorna -1, indicando um erro, pois a chave já existe na lista.
            if L[i] == k:
                return -1
            else:
                # Caso contrário, a posição de inserção é encontrada na lista.
                posInsercao = i
                # Sair do loop, pois a posição de inserção foi encontrada.
                i = n + 1
        else:
            # Se o elemento atual for menor que 'k', continue procurando na próxima posição.
            i = i + 1

    if i == n:
        # Se a busca chegar ao final da lista sem encontrar uma posição, a inserção será no final da lista.
        posInsercao = n

    L.append('')  # Aumenta o tamanho da lista adicionando um espaço vazio.
    i = n  # Inicializa 'i' para começar o ajuste da lista.

    while i > posInsercao:
        # Empurra cada nó para o final da lista, criando espaço para a inserção.
        L[i] = L[i - 1]
        i = i - 1

    L[posInsercao] = k  # Insere o novo elemento na posição encontrada.
    # Retorna a posição de inserção do novo elemento na lista.
    return posInsercao
    # saída normal da função


numeros = [1, 2, 3, 4, 6, 7, 8, 9, 10]
print(numeros)
insereOrdenada(5, numeros, len(numeros))
print(numeros)


def removeL(k, L, n):
    i = 0  # Inicializa um índice para buscar o nó a ser removido.
    posRemocao = -1

    while i < n:
        if L[i] == k:
            posRemocao = i  # Chave encontrada
            i = n + 1  # Sair do loop
        else:
            if L[i] > k:
                return -1  # Erro, a chave não existe
            i = i + 1

    if i == n:
        return -1  # Erro, a chave não existe

    i = posRemocao  # Início do ajuste da lista
    while i < n - 1:
        L[i] = L[i + 1]  # Puxa cada nó posterior 1 posição
        i = i + 1

    L.pop(n - 1)  # Ajusta o tamanho da lista, removendo o último elemento
    return posRemocao  # Saída normal da função, retorna a posição da remoção


nomes = ['Joao', 'Maria', 'Ana', 'Arthur']
i = removeL('Arthur', nomes, len(nomes))
print(nomes)


#Lista encadeada ou Lista em nós

class No:
    def __init__(self, chave, valor):
        self.chave = chave
        self.valor = valor
        self.proximo = None


class ListaEncadeada:
    def __init__(self, cabeca=None):
        self.cabeca = cabeca

    def print(self):
        current = self.cabeca
        while current:
            print(current.valor)
            current = current.proximo

def busca(self, k):
    noAtual=self.cabeca
    if noAtual.chave==k:
        return noAtual                #chave encontrada
    while noAtual.proximo != None:
        noAtual=noAtual.proximo       #passe para próximo nó
        if noAtual.chave==k:
            return noAtual             #chave encontrada
    
    return None 

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Criando uma lista encadeada e adicionando elementos
my_list = LinkedList()
my_list.append(1)
my_list.append(7)
my_list.append(3)

# Exibindo a lista encadeada
my_list.display()
