#join unir strings

lista = ['João', 'Paulo', 'II' ]
nome = ' --- '.join(lista) #fica entre os espaços da lista, transformando-a em string
print(nome) #saida: João ---- Paulo --- II
#Ótimo para formatação de data usando a barra /, mas os numeros devem ser strings

#montar uma data valida com a lista abaixo
lista = ['2023','23', '12']
nome = "/".join(lista)
print(nome)