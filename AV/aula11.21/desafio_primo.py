# Solicitar ao usuário um número inteiro positivo
numero = int(input("Digite um número inteiro positivo: "))

# Verificar se o número é primo ou não
if numero > 1:
    eh_primo = True
    for i in range(2, numero):
        if numero % i == 0:
            eh_primo = False
            break

    if eh_primo:
        print(f"{numero} é um número primo.")
    else:
        print(f"{numero} não é um número primo.")
else:
    print("Por favor, digite um número inteiro positivo maior que 1.")
