entrada = input('[E] para entrar e [S] para passar: ')
senha_digitada = input('Digite a senha: ')
senha = "12345678"

if(entrada == 'E' or entrada == 'e'):
    if(senha == senha_digitada):
        print("Sucesso")
    else:
        print("Senha Incorreta")
elif(entrada == 'S' or entrada == 's'):
    if(senha == senha_digitada):
        print('Você escolheu PASSAR')
    else:
        print("Você não passou, senha incorreta")
else:
    print("Você não selencionou uma opção válida!")