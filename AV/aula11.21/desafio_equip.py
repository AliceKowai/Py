aumento_anual = 0.3
inicial = 100
contador = 0
valorFinal = inicial

while True:
    aumento = valor_final * aumento_anual  
    valor_final = valor_final + aumento  
    contador += 1  

    if valor_final >= 200:
        print(f"Leva {contador} anos para atingir um valor de {valorFinal}")
        break
