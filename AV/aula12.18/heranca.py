#classe estendida é referente a super classe, ou seja quando falar em estender, fazer uma subclasse
#exemplo de super classe estudante : subclasses, estudante pós / estudante graduação
#dander metodo => __metodo__
class Estudante:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

class EstudanteGraducao(Estudante):
    def __init__(self, nome, matricula, curso):
        super().__init__(nome, matricula)
        self.curso = curso

class EstudantePos(Estudante):
    nivel = 1
    orientador = 'Professor Carlos Roberto'

aluno = EstudanteGraducao('Alice', 232345, 'CC')
print(aluno.matricula)