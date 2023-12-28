nome = input("Nome: ")
nome2 = input("Nome: ")
nome3 = input("Nome: ")
nome4 = input("Nome: ")
nome5 = input("Nome: ")

lista_nomes = []
lista_nomes.append(nome)
lista_nomes.append(nome2)
lista_nomes.append(nome3)
lista_nomes.append(nome4)
lista_nomes.append(nome5)
print(lista_nomes)

if(lista_nomes[0][0] == "A" or lista_nomes[1][0] == "E" or lista_nomes[2][0] == "I") or lista_nomes[3][0] == "O" or lista_nomes[4][0] == "U":
    print("Seu nome inicia com uma vogal")

lista_nomes.insert(0,'cu')
print(lista_nomes)