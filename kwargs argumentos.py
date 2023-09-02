def minha_funcao(**kwargs):
    for chave, valor in kwargs.items():
        print(f"a chave é {chave} e o valor é {valor}")
    print(type(kwargs))
    
minha_funcao(nome="carlos", idade=18, país="brasil")