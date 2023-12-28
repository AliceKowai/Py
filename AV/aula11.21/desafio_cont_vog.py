palavra = input("Digite uma palavra: ")
vogais = 'aeiouAEIOU'
contagem = 0

for letra in palavra:
    if letra in vogais:
        contagem += 1

print(f"A palavra '{palavra}' tem {contagem} vogais.")
