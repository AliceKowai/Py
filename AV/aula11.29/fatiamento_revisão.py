#fatiamento regras [inicial:final:passo] passo ou pulo
#pegar o meio de uma palavra e retirar - fatiar, tipo Paulo ficaria Palo
#Quando o step, passo, pulo, está negativo, quer dizer que muda a direção do passo
variavel = "Paulo"
print(variavel[2:4])

variavel = "Azul é a cor da parede de Deus"
print(variavel[0:4])
print(variavel[-4:]) #tem que colocar assim quando quiser pegar o ultimo elemento junto, pois se colocar -1, ele não entra
 #Ultilizando fatiamento e repetição, imprima uma lista até o e removendo uma lista de cada vez

contador = 5
contadorloop2 = 1
alfabeto = ["a","b","c","d","e"]
while True:
    print(alfabeto[0:contadorloop2])
    contadorloop2 = contadorloop2 + 1
    if contadorloop2 == len(alfabeto):
        break
while True:
    print(alfabeto[0:contador])
    contador = contador - 1
    if contador == 0:
        break


lista = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

for i in range(len(lista)):
    lista[:len(lista)-i]
