#crie abstração para uma classe funcionario com duas subclasses

class Funcionario:
    def __init__(self, nome, cpf, salario):
        self.nome = nome
        self.cpf = cpf
        self.salario = salario
    
class FuncionarioHorista(Funcionario):
    def __init__(self, nome, cpf, horas_trabalhadas, valor_horas):
        super().__init__(nome, cpf, salario = None)
        self.horas_trabalhadas = horas_trabalhadas
        self.valor_horas = valor_horas
    def __str__(self) -> str:
        return (f'Nome: {self.nome} \nCPF: {self.cpf} \nSalario: {self.salario if self.salario !=None else "O salario deve ser calculado primeiro"}')
    def calcular_salario(self):
        self.salario = self.valor_horas * self.horas_trabalhadas
        
class FuncionarioMensal(Funcionario):
    def __init__(self, nome, cpf, salario):
        super().__init__(nome, cpf, salario)
    def __str__(self):
        return f'Nome: {self.nome} \nCPF: {self.cpf} \nSalario: {self.salario}'
    def calcular_salario(self):
        valor_hora = self.salario / 40
        self.salario = self.salario + (valor_hora * self.horas_extras)

    
funciona_hour = FuncionarioHorista('Alice', 12345678912, 40, 20)
print(funciona_hour)
funciona_hour.calcular_salario()
print(funciona_hour)
funciona_men = FuncionarioMensal('Gus', 123463353, 1500)
print(funciona_men)