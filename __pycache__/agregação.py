class estudante:
    def __init__(self, nome):
        self.nome = nome

class turma:
    def __init__(self, nome):
        self.nome = nome
        self.estudante = []

    def adicionar_estudantes(self, estudante):
        self.estudantes.append(estudante)

joão = estudante("joão")
maria = estudante("maria")

turmaA = turma ("turma A")
turmaA.adicionar_estundate(joão)
turmaA.adicionar_estudante(maria)


        