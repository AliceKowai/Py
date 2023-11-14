alunos_back = ["Alice", "Mikael", "Geisa", "Arthur", "Meyva"]
print(alunos_back)
alunos_back.append("Gabriel")
#print(alunos_back)
del alunos_back[2]
#print(alunos_back)
alunos_back.remove('Arthur')
#print(alunos_back)
print(alunos_back)
alunos_back.append('Jefferson')
alunoRemovido = alunos_back.pop()
print("aluno removido:",alunoRemovido)