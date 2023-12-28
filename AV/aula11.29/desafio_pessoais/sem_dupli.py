# Solução do Desafio 3
def remover_duplicatas(lista):
    lista_sem_duplicatas = []
    for item in lista:
        if item not in lista_sem_duplicatas:
            lista_sem_duplicatas.append(item)
    return lista_sem_duplicatas

# Exemplo de uso:
lista = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]
lista_sem_duplicatas = remover_duplicatas(lista)
print(lista_sem_duplicatas)
