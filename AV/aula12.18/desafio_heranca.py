#self.__class__.__name__ mostra o nome da classe
class Pessoa:
    def __init__(self, nome):
        self.nome = nome
    
    def __str__(self):
        return (self.nome)

class Empregado(Pessoa):
    def __init__(self, nome, cargo, salario):
        super().__init__(nome)
        self.cargo = cargo
        self.salario = salario

class Estudante(Pessoa):
    def __init__(self, nome, matricula):
        super().__init__(nome)
        self.matricula = matricula

class estudante_graduacao(Estudante):
    def __init__(self, nome, matricula, curso):
        super().__init__(nome, matricula)
        self.curso = curso
    def __str__(self):
            return(f'nome: {self.nome} \nmatricula {self.matricula} \ncurso: {self.curso}')


class estudante_pos(Estudante):
    def __init__(self, nome, matricula, orientador, nivel):
        super().__init__(nome, matricula)
        self.orientador = orientador
        self.nivel = nivel
    def __str__(self):
        return(f'nome: {self.nome} \n matricula {self.matricula} \n orientador {self.orientador} \n nivel {self.nivel}')

aluno = estudante_graduacao('Alice', 235243, 'CC')
aluno2 = estudante_pos('Paulo', 42452, 'Juazeiro', 1)
print(aluno)
print(aluno2)