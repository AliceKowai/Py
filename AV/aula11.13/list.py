#list - lista - caracteristica: mutavel ou iteravel - suporta vários tipos - metodos e fatiamentos. Ela possui indices.
#obs: Quando uma lista é definida com apenas um tipo, ela é considerada unitária.

#obs todo metodo por obrigação retorna algum valor
# len metodo que retorna a quantidade de itens de uma lista
#append - metodo que insere itens no final da lista
# del - remove item especifico no final da lista - pelo o indice
# remove - remove um objeto especificado da lista - pelo o valor
# pop - remove o último elemento da lista
# insert - adiciona um elemento no inicio da lista

lista = []
print(lista, type(lista))
print(len(lista))
print("***" * 20)
lista = ['Front']
print(len(lista), lista) #len mostra o tamanho da lista
lista.append('Back')
lista[1] = 'Data Science' #adicionando o data science
#Indices  0          1     2   3     4
#inverso  -5       -4     -3   -2    -1
lista = ['back', 'tarde', 21, True, 8.8] #linha mista
print(lista, len(lista))
lista[1] = ['computador', 'copo', 'caneta'] #adicionando a lista dentro da lista no indice 1
print(lista[1][2])
print(lista)
del lista[-2]
lista.remove('back')
print(lista)
lista.pop() # é possivel guardar o valor removido com o pop, atribuido a lista.pop() a alguma variavel
print(lista)
lista.insert(0,'Amontada Valley')
print(lista)
lista.insert(2,'professor')
print(lista)
lista.insert(200,'Aluna')
print(len(lista))
print(lista)
print(lista[4])

