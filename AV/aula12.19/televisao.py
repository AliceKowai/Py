class Televisão:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.canal = 0
        self.ligada = False
    def __str__(self):
        return f'Tamanho: {self.tamanho}| Status: {self.valida_ligada()} | Canal: {self.canal}'
                #{self.salario if self.salario !=None else "O salario deve ser calculado primeiro"}

    
    def get_tamanho(self):
        return self.tamanho
    def get_canal(self):
        return self.canal
    def get_ligada(self):
        return self.ligada
    
    def set_tamanho(self, novo_tamanho):
        self.tamanho = novo_tamanho
    
    def ligar(self):
        if (self.ligada == True):
            print('A Televisão já está ligada')
            return
        self.ligada = True

    def desligar(self):
        if (self.ligada == False):
            print('A Televisão já está desligada')
            return
        self.ligada = False
        self.canal = 1
    
    def mudar_canal(self, novo_canal):
        if self.ligada == False:
            return
        if self.canal == novo_canal:
            print(f'Já está no canal {self.canal}')
            return
        if novo_canal < 0 or novo_canal > 200:
            print('Canal inexistente, por favor, outro canal, bixo')
            return
        self.canal = novo_canal
        print(f'mudou para o canal {self.canal}')

    def valida_ligada(self):
        if self.ligada:
            return 'Ligada'
        else:
            return 'Desligada'

    def set_canal(self, novo_canal):
        if self.ligada == True and novo_canal >= 0 and novo_canal<=999:
            self.canal = novo_canal

televisão = Televisão(29)
print(televisão)
            
televisão.ligar()
print(televisão)
televisão.mudar_canal(3)
print(televisão)
televisão.desligar()
print(televisão)


