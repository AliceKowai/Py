salario_atual = float(input("Digite o salario atual: "))
reajuste = float(input("Digite o reajuste em porcentagem (%): "))

salario_apos_reajuste = ((reajuste / 100) * salario_atual) + salario_atual

print(f"{salario_apos_reajuste}")
