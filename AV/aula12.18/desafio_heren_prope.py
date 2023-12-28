class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.__cpf = None
    def __str__(self):
        return f'Nome: {self.nome}, Idade: {self.idade}, e CPF: {self.__cpf}'
    def get_cpf(self):
        return self.__cpf
    def set_cpf(self, meu_cpf):
        self.__cpf = meu_cpf

class Professor(Pessoa):
    def __init__(self, nome, idade, salario, disciplina, cpf):
       super().__init__(nome, idade)
       self.salario = salario
       self.disciplina = disciplina
       self.cpf = super().set_cpf(cpf)
    def __str__(self):
        return f'Nome: {self.nome}, Idade: {self.idade}, e CPF: {super().get_cpf()}'


class Aluno(Pessoa):
    pass

gugs = Professor('Gustavo', 21, 1200, 'poo', 234565334 )

gugs.set_cpf(12345678911)
print(gugs)

