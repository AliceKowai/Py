import os

nome="teste.txt"
nome2="teste2.txt"
caminho="C:/Users/alice/Documents/Py/IntensivaoPy/"
f=open("C:/Users/alice/Documents/Py/IntensivaoPy/"+nome,"at")
#g=open(caminho+nome2,"w")

#r - read - leitura
#a - append - anexar
#w - write - escrita
#x - create - criar
#t - texto
#b - binario
## Esses valor devem ser modificados no endereço do open ###

f.write("Jesus ajuda!")
f.write("\nJesuuus, o filho da Rainhaaa")
#g.write("Agora Deletar")

if os.path.exists(caminho+nome2):
    print("arquivo existe")
else:
    g=open(caminho+nome2,"x")
    g.close()


os.remove(caminho+nome2)




f.close()





age = 36
txt = "My name is John, and I am {}" #{} concatenação de variaveis, depois só chamar a função format(variavel)

print(txt.format(age))
print(10 < 9)
fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)
print(fruits)