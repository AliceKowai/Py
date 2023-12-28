contador = 1
while contador <= 6:  
    idade = int(input("Digite sua idade: "))
    if idade > 13:
        print(f'aluno {contador} tem mais de 13 anos.')
    contador += 1
print('fim')

while True:
    nota = int(input("Digite uma nota de 0 a 10: "))
    if(nota < 0 or nota>10):
        break