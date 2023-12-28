def encontrar_menor(a, b, c):
    if a < b and a < c:
        return a
    elif b < a and b < c:
        return b
    else:
        return c

# Entrada dos valores a, b e c
a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

# Chamada da função e exibição do menor número
menor_numero = encontrar_menor(a, b, c)
print("O menor número é:", menor_numero)
