# Interpolando strings com codigo python
nome = input("Qual é seu nome? ")
#concatenação
print("Seja muito bem-vindo,", nome)

#Interpolação
print(f'Seja muito bem-vindo, {nome}. Estavámos esperando por você!!!')
print("Data {:02d}/{:02d}".format(1,11))  #formatando a data