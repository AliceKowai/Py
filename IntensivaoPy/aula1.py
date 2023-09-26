x= 1
x=("Carro", "avião", 1, 43.5, True) #array é [] tupla é (), nessa caso é uma tupla, as 
n1=5; n2=2;x=complex(n1,n2) #tipo de dados: numeros complexo, numero imaginario e real
#print(x.real) #forma de acessar a parte real, no caso n1 é real
#print(x.imag) 
x= {            #dicionario
    "Nome": "Alice",
    "Gato": "Floki",
    "Anime": "Naruto"
}

x = " Uma cadeia de caracters "
#print("valor", x["Gato"]) forma de acessar um elemento dentro do dicionario
#print("Valor de x é:", x)
#print("Tipo é:", type(x)) função tipo
#print(x[0:6]) de um indice até outro indice 
#print(x.strip()) tira os espaços inicial e final
#print(x.lower().strip()) usar duas funções 
#print(len(x)) tamanho da cadeia, array
#funções replace - sintaxe array.replace("troca esse que existe","por esse"), função split corta a cadeia de caracteres e transforma em uma lista, sintaxe cadeiaDeCaracteres.split(" ")


Floki = "Meu gato branquinho"
palavra = "gato"
res=palavra.upper() in Floki.upper() #pesquisar uma palavra em uma cadeia de strings fazendo a conversao para mausculo para que ache a palavra
print(res)

#função format ex: 
data = "{}, {} de {} de {}" #como usar data.format(variavel1, variavel2, variavel)
gatos = ["Flokin", "Pipoca", "Totoro", "Soga"]
#gatos.remove("Pipoca")
gatos.append("Branco") #adicionar item a lista
#gatos.pop() remove o ultimo elemento da lista
del gatos[2]
#gatos.clear() #remove todos
gatos2 = list(gatos)
print(len(gatos2), gatos2)