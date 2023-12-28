#Não tem indice, não garante a ordem dis elementos, são iteraveis (for, in, not in) são mutaveis mas só aceitam tipos imutaveis, não podem ter elementos duplicados.
#metodos add(), update(), clear() e discard()
#Criando um set: set('Alice') ou {1,3,5,7}

##### {} ##### Forma é a chaves

set01 = set('Alice')
set02 = set('Aaaab') #saida 'A','b', 'a' Pois ele conta o mesmo caracter apenas uma vez
set03 = {'Floki', 'Branquinho', 'Cinzenta', 'Nepo', 'Sombras'} #Essa é a forma de fazer o set sem o metodo set()
lista = [1,2,3,4,5,6,7,8,9,0]
set04 = set(lista)
print(set01)
print(set02)
print(set03)
print(set04)

#for i in set04:
    #print(i)

set03.add('Zarami')
set03.update('Zarami') #Quebra o que foi passado e transforma em caracteres e adiciona no set
set03.discard('Zarami')
#set03.clear() Limpa/ torna vazio, tira os elementos
print(set03)

set06 = set03 | set04 #união de conjuntos
set07 = set03 & set04 #comum, intersecção
set08 = set03 - set04 #comum, intersecção

print('------------')
print(set08)