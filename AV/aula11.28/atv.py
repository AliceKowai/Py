def num_inv(numero):
    numero_inverso = numero[::-1]
    return int(numero_inverso)
numero = input('Digite um número: ')
print(f'O número informado foi {numero} e o seu reverso é {num_inv(numero)}')
print('#################')

###############################################################################

def numero_reverso(numero):
    reverso = 0
    while numero > 0:
        #pegar ultimo numero
        ultimo_valor = numero%10 #numero%10 == pega o numero depois da virgula numero //10 pega o depois da virgula
        #adicionar ultimo numero
        reverso = (reverso * 10) + ultimo_valor
        #tira o ultimo valor
        numero = numero //10
        print(reverso)
        return reverso
        
numero = int(input('Digite um número: '))
print(numero_reverso(numero))