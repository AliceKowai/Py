# Listas são conjunto de elementos []
# polimofismo - É a capacidade de alguma coisa ser ultilizada de varias formas em varias situações
# extend
lista_a = [1, 2, 3, 4, 5]
lista_b = [6, 7, 8, 9, 10]

#o Sinal + ele soma números e concatena string

a = 2
b = 3
print(a + b)

c = 'Amontada'
d = 'Valley'
print(c+d)

#soma listas
print(lista_a + lista_b)

# metodo extends muda a propria lista que foi executada o metodo 
#adiciona uma lista na outra

lista_a.extend(lista_b)

print(lista_a)