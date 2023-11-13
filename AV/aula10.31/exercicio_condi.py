distancia = int(input("Distância em km: "))
litros = int(input("Litros de gasolina: "))
consumo = distancia/litros
if consumo < 8:
    print("Venda o carro", consumo)
elif consumo >=8 and consumo <= 14:
    print("Economico", consumo)
elif consumo > 14: 
    print("Super economico", consumo)
else:
    print("Consumo não indetificado")