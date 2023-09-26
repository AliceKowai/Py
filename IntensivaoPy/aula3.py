n1=int(input("Digite o primeiro numero: "))
n2=int(input("Digite o segundo número: "))
def somar():
    r=n1+n2
    print("A soma de", n1, " + ", n2, " = ", r)
def subtrair():
    r=n1-n2
    print("A soma de", n1, " - ", n2, " = ", r)

def Calculos():
    somar()
    subtrair()
Calculos()

## funções com parametros ##

def multiplicar(n1, n2):
    r=n1*n2
    print("A soma de", n1, " x ", n2, " = ", r)

multiplicar(5,7)


#argumentos arbitrarios
def textos(*txt):
    for t in txt:
        print(t)

textos("Atenção", "Calma!", "Não", "Sim...", "Silêncio")

def soma(*num):
    r=0
    for n in num:
        r+=n
    print("Divisão = ", r)

soma(2,5,3,2,4,2,3,4,3,3,3,)

## função com valor padrão ##

def bf(b="solidão"):
    print("Meu namorado se chama:", b)

bf()

## return ##

## função lambda ou função anonima ##

quadrado=lambda a: a ** 2
print(quadrado(9))

r=lambda x,func: x+func(x) #usar função como parametro
res=r(8,lambda x:x*x)
print(res)