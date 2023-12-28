# Lista de nomes fornecida pelo usuário
nomes = ["Ana", "Pedro", "Alice", "André", "Mariana", "Antônio", "Amanda"]

# Contador para nomes iniciados com 'A'
contagem_nomes_a = 0

# Verificando quantos nomes começam com 'A'
for nome in nomes:
    if nome[0] == 'A' or nome[0] == 'a':
        contagem_nomes_a += 1

print(f"Existem {contagem_nomes_a} nomes na lista que começam com a letra 'A'.")
