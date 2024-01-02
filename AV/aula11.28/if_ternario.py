#salario = float(input('Informe o valor do seu salario: '))
salario = 1
if salario >= 2500.00:
    print('IR sera cobrado')
else:
    print('IR nao sera cobrado')

variavel_controle = 'IR será cobrado' if salario >= 2500.00 else 'IR não será cobrado'
#print(variavel_controle)
                              ###### elif ######  
vr_controle = 'ok 1' if False else 'ok 2' if True else 'Fim'

# vr_controle como ela seria na estrutura if normal
if True:
    print('OK 1')
elif True:
    print('OK 2')
else: 
    print('Fim')

print(vr_controle)