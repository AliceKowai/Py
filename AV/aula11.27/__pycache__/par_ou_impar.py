jogador1 = input('Escolha par ou impar: ').lower()
jogador2 = ''
if jogador1 == 'par':
    jogador2 == 'impar'
else:
    jogador2=='par'
numero_jogador1 = int(input('Digite um número: '))
numero_jogador2 = int(input('Digite um número: '))
numero = numero_jogador1 + numero_jogador2
if numero %2 ==0:
    if jogador1 == 'par':
        print('jogador numero 1 venceu')
    else:
        print('jogador numero 2 venceu')
else: 
    if jogador1 == 'impar':
        print('jogador 1 venceu')
    else: 
        print('jogador 2 venceu')

