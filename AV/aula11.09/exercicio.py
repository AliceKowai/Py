#1. Faça o fatiamento de 10 palavras do texto abaixo.
#Faça o fatiamento de 8 palavras e monte uma frase com a impressão dessas palavras.
# [i:f:p]

texto = "Somos uma escola de tecnologia de informação que cria pontes entre pessoas, conhecimento e empresas. Ambiente que proporciona conexão, troca de conhecimentos e aprendizado compartilhado entre participantes, instrutores e empresas parceiras"

print('Somos', 'informação', 'cria', 'pessoas', 'Ambiente', 'conexão', 'troca', 'entre', 'que', 'escola' in texto)
print('----------------')
print("1",texto[0:5])
print("2",texto[10:16])
print("3",texto[20:30])
print("4",texto[36:44])
print("5",texto[49:53])
print("6",texto[54:60])
print("7",texto[67:74])
print("8",texto[76:89])
print("9",texto[91:99])
print("10",texto[101:110])
print('-----')

# Palavras específicas
palavra1 = texto[10:16]
palavra2 = texto[17:19]
palavra3 = texto[20:30]
palavra4 = texto[126:135]
palavra5 = texto[160:172]
palavra6 = texto[172:185]
palavra7 = texto[61:66]
palavra8 = texto[67:74]


# Imprimindo as palavras
print(palavra1, palavra2, palavra3,":", palavra4, palavra5, palavra6, palavra7, palavra8)

