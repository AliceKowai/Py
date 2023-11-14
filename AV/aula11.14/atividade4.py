letra1 = input("Digite a letra 1: ")
letra2 = input("Digite a letra 2: ")
letra3 = input("Digite a letra 3: ")
letra4 = input("Digite a letra 4: ")
letra5 = input("Digite a letra 5: ")
lista_consoantes = []
number = type(1)
numberFloat = type(1.2)

if(number == type(letra1) and letra1 != "a" and letra1 != "A" and letra1 != "e" and letra1 != "E" and letra1 != "I" and letra1 != "i" and letra1 != "o" and letra1 != "O" and letra1 != "u" and letra1 != "U" ):
    print("É uma consoante: ")
    lista_consoantes.append(letra1)
if(letra2 != "a" and letra2 != "A" and letra2 != "e" and letra2 != "E" and letra2 != "I" and letra2 != "i" and letra2 != "o" and letra2 != "O" and letra2 != "u" and letra2 != "U" ):
    print("É uma consoante: ")
    lista_consoantes.append(letra2)
if(letra3 != "a" and letra3 != "A" and letra3 != "e" and letra3 != "E" and letra3 != "I" and letra3 != "i" and letra3 != "o" and letra3 != "O" and letra3 != "u" and letra3 != "U" ):
    print("É uma consoante: ")
    lista_consoantes.append(letra3)
if(letra4 != "a" and letra4 != "A" and letra4 != "e" and letra4 != "E" and letra4 != "I" and letra4 != "i" and letra4 != "o" and letra4 != "O" and letra4 != "u" and letra4 != "U" ):
    print("É uma consoante: ")
    lista_consoantes.append(letra4)
if(letra5 != "a" and letra5 != "A" and letra5 != "e" and letra5 != "E" and letra5 != "I" and letra5 != "i" and letra5 != "o" and letra5 != "O" and letra5 != "u" and letra5 != "U" ):
    print("É uma consoante: ")
    lista_consoantes.append(letra5)

print(lista_consoantes)
print(number)