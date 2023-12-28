#For - é uma estrutura de repetição, um ponto a ser observado é que o "for' ele deve ser utilizado em casos que você sabe a quantidade de repetições. 
#na grande maioria das vezes você vai utilizar o metodo RANGE() para montar a chamada do "for"
#range(i, f, s) - i = INICIO, f = FIM, s = STEP(salto)
#Obs: voc~e não é obrigado a passar os três valores do range. Caso passe apenas um valor ser considerado como valor do FIM.
#   ---- range(5) ------
#   ---- range(1, 5) ---
#iter() - transforma um objeto em iteravel
#next() - função para imprimir os iteraveis de uma "lista".

#enumerate() é um iterador de indices e valores

lista_nomes = ['Lotric', 'Floki', 'Sombras', 'Nepo', 'Lancer']
lista_enumerada = enumerate(lista_nomes)
print(lista_nomes)
print(lista_enumerada)
#transformar em lista list(lista_enumerada)
print(list(lista_enumerada))
for item in lista_enumerada:
    print(item)

for indice_lista, item_lista in enumerate(lista_nomes):
    print(indice_lista)