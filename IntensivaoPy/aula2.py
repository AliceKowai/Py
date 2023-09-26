#condicionais
dormir = True

if dormir:
    print("To com sono")
print("Trabalhar") 

a = 5
b = 4
res = 0 
op = "-"
if op == "+":
    res = a + b
elif op == "-":
    res = a - b
elif op == "*":
    res == a * b
elif op == "/":
    res == a / b
else: 
    print("Operador invalido")

print(a, op, b, "= ",    res)


nome = input("digite seu nome: ")
print(nome)

# && == AND tmb tem o OR == ||

##### loops ####

gatos = ["Flokin", "Pipoca", "Totoro", "Soga"]
for gato in gatos:
    if(gato == "Totoro"):
        break
    print(gato)

palavra = input("Digite uma palavra").upper()
while palavra[0] != "A":
    palavra = input("Digite uma palavra novamente").upper()

print(palavra)


## Dupla ##

t_gatos = tuple(gatos)
print(gatos)

gatos_m = [
     ["Nome", "Flokin"],
     ["Cor", "Branca"],
     ["Idade", 1]
]

gatos_m.append(["Temperamento", "Carinhoso e brincalhão"])

for l, c in gatos_m:
    print(l, c)


## Dictionary ## 

pessoa = {
    "nome": "Alice",
    "Altura": "1,60",
    "Cor": "Desconhecido",
    "Peso": "53kg"
}

pessoa["Cor"] = "Parda" #mudar um valor que já existe
pessoa["Habilidade"] = "desconhecido" #adicionar uma nova chave e valor

for c,v in pessoa.items():
    print(c,": ", v)

if "nome" in pessoa:
    print(pessoa["nome"])