#observar a possibilidade de não repetições
# while = enquanto
#contador
#while condição:
#    codigo
#   implementar o contador
#break = quebra as estruturas de repetição

contador = 0
while contador < 30:
    print(contador)
    contador+=1
    if contador == 12:
        print('cheguei no 12')
    if contador == 20:
        break
print('Saiu do while')