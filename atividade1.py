class turmas:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
         
    def texto(self):
        print(f"meu nome é {self.nome} minha idade é {self.idade}")

Aluno00 = turmas("carlos", "18")
      
print(Aluno00.nome)
print(Aluno00.idade)
Aluno00.texto()