#mutaveis - são valores que poder ter seu valor alterado na menmoria do dispositivo
#imutaveis são dados que so podem ser copiados da memoria do dispositivo


lista = ['Alice', 'Gus']
lista[1] = 'Floki'
print(lista)
nome = 'Gus'
nome = 'Alice'
#nome[2]= 'a'  erro, não dá para mudar o valor dentro da estrutura da variavel
print(nome)
print(lista)
listab = lista.copy() #COPIAR LISTTA - pois dizer que lista é igual a lista, atribuindo valor apenas cria um ponteiro e qualquer modificação será feito nas duas.
#O Copy existe para criar outro espaço de memoria em vez de um ponteiro.
listab[0] ="Cu"
print(lista, "------", listab)