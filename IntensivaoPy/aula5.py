## Try Except --- Tratamentos de erros ##
x="cu"
try:
    print(x)
except NameError:
    print("Name Error")
except:
    print("Error")
else:
    print("sucesso")
finally:
    print("Fim")

#exceção a um erro com exception
num = -10

if num < 1:
    raise Exception("Valor não permitido")
if not type(num) is int:
    raise Exception("Somente numeros permitidos")
else:
    print(num)