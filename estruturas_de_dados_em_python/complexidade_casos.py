def fatorial(n):
    if n == 1:
        print('if',n)
        return 1
    else:
        chiclete = 1
        fator = n * fatorial(n - 1)
        print('else:', n, 'fator:', fator)
        return fator


print(fatorial(6))