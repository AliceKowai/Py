nome = 'Alice'
print('al' in nome)

print('='*20)
seu_nome = input("Informe seu nome: ")
buscar = input("Informe o valor a ser encontrado: ")

if(buscar in nome):
    print(f'{buscar} está contido em {seu_nome}')
else:
    print(f'{buscar} NÃO está contido em {seu_nome}')

#not in

# Definindo uma string
frase = "Olá, como vai?"

# Verificando se a letra 'z' não está na string
if 'z' not in frase:
    print("A letra 'z' não está na string.")
else:
    print("A letra 'z' está na string.")
