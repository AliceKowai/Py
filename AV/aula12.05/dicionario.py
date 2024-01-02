#dicionario não é ordenado
#Uma nova chave pode entrar em qualquer lugar
d = {'user': 'AliceKowai', 'password':'secret', 'musica': 'musica final do ai solium files'}
print(d)
# del d[key], deleta pela a chave, pois valores pode ter iguais
# keys() lista de chaves, 
# values() lista com valores, 
# items(), traz tanto chave quanto valor
# get(), pega algo do dicionario
# update() atualizar
# copy() copiar dic
# sorted() ordena um dicionario na ordem crescente
# sorted(d,key = get, reverse= True) ordena na ordem decresente


pessoa = {'nome': 'Paulo',   #se tiver valor repetido, ele ignora, se as chaves tiverem nome iguais, mesmo que haja valores iguais, ele identifica como 1
          'sobrenome1': 'Junior',
          'sobrenome': 'Junior',
          'sobrenome': 'Junior2',
          'sobrenome': 'Junior',
          'idade': 12
          }
print(len(pessoa))
print(pessoa.keys()) #retorna uma lista com as chaves
print(pessoa.values()) # """"""   com os valores
v = pessoa.values()
print("****" * 20)
for i in pessoa:
    print(i)
print("****" * 20)
for i in v:
    print(i)

print("****" * 20)

for chave, valor in pessoa.items():
    print(chave, valor)

print("****" * 20)

print(pessoa['idade'])

print("****" * 20)

d1 = {'valor1': 100,
      'valor2': 200,
      'valor3': 300,
      }
d2 = d1.copy()
print(d1)

d2['valor2'] = 2000 #modificando um valor no dicionario, nota: se um dicionario receber o valor de outro, ele criará apenas um ponteiro, só copia se usar o copy()

print(d2.get('valor2'))

d3 = d1.pop('valor3') #obrigatorio passar argumento
print(d1)

lista = [1,2,3]
d1.update(d2)
#print(d1.has_key("valor5"))

dic = {}

print(type(dic))


