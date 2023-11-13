nome = "Gustavo"
salario = 4500.99

print(nome, "ganha um salario de R$", salario)
print(f'{nome} ganha {salario} quem dera')

#forma FORMAT de imprimir
#s - string
#d e i - int
# f - float
# x e X - hexadecimais

print('O salário de %s é R$ %.2f' %(nome, salario))
print('Quem ganha um salário de R$ %.2f é o %s' %(salario, nome))