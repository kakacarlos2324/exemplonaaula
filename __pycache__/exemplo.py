class turma:
    def __init__(self, nome, sobrenome):
        self.nome= nome
        self.sobrenome = sobrenome
        
    def texto(self):
            print(f"o meu nome é {self.nome} e meu sobrenome é {self.sobrenome}")
            
aluno1 = turma("carlos", "gabriel")
        
print(aluno1.nome)       
print(aluno1.sobrenome)
        
aluno1.texto()