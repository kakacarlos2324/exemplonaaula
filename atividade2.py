class livros:
    titulo = "casa doida"
    autor  = "carlos"
    ano_publicaçao = "2023"
    
    def __init__(self, titulo, autor, ano_publicaçao):
     self.titulo = titulo
     self.autor = autor
     self.ano_publicaçao = ano_publicaçao

    def descricao(self):
      print(f"o titulo é {self.titulo} o autor é {self.autor} o ano_publicaçao é {self.ano_publicaçao}")

livros1 = livros("casa doida", "carlos", "2023")    
livros2 = livros("tudo louco", "joão", "2030")

livros1.descricao()
livros2.descricao()