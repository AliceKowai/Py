import random
import os
erros=0
sorteado=random.randrange(0,100)
jogador=int(input("Digite seu número: "))
while(sorteado!=jogador):
    os.system('cls')
    if(sorteado>jogador):
        print("Errou, o numero é maior")
    elif(sorteado<jogador):
        print("Errou, o numero é menor")
    erros+=1
    jogador=int(input("Digite seu número: "))
print("Acertou em ", erros, " tentativas")