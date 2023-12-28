# Solicitar ao usuário um número inteiro positivo
numero = int(input("Digite um número inteiro positivo: "))

# Verificar se o número é um número perfeito
soma_divisores = 0
for i in range(1, numero):
    if numero % i == 0:
        soma_divisores += i

# Exibir mensagem indicando se o número é um número perfeito ou não
if soma_divisores == numero and numero != 0:
    print(f"{numero} é um número perfeito.")
else:
    print(f"{numero} não é um número perfeito.")
