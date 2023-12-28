dic_acesso = {'Alice': '1234', 'Floki':'miau', 'Uni': 'auau'}
user_pass = {}
usuario = input('Informe seu nome de usuario: ')
senha = input('Informe sua senha: ')
user_pass[usuario] = senha #atribui as variaveis a chave atrelado com o valor 
#e adiciona no dicionario

for chave in dic_acesso.keys():
    if chave == usuario:
        print(f'Olá,{usuario}')
        if dic_acesso[chave] == senha:
            print('Acesso Liberado! ')
            break
        else:
            print(f'A senha está incorreta.')
            break
else:
    print('O usuario ou senha está incorreto') #Se não break, entra