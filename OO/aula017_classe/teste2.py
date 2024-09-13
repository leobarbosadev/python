class ClassePai:
    def __init__(self, a, b):  # metodo construtor
        # iniciar os atributos
        self.a = a
        self.b = b


class ClasseFilha(ClassePai):
    def __init__(self, a, b):  # metodo construtor da classe pai
        # iniciar os atributos
        self.a = a
        self.b = b

    def metodo_classe_filha(self):
        print('Subtracao')
        subtracao = self.a - self.b
        print(f'O resultado é: {subtracao}')


# instaciando um objeto e passando valores para os atributos
exibir = ClasseFilha(10, 2)
exibir.metodo_classe_filha()


class ClassePai: # Criacao da classe pai
    def __init__(self, a, b): # metodo construtor
        # iniciar os atributos
        self.a = a
        self.b = b
        
class ClasseFilha(ClassePai): # classe filha herda classe pai
    def __init__(self, a, b): # metodo construtor da classe pai
        # iniciar os atributos
        self.a = a
        self.b = b
        
    def metodo_filho(self): # metodo da classe filha
        print('Soma')
        soma = self.a + self.b
        print(f'A some é {soma}')
        
objeto = ClasseFilha(10, 2) # instanciando o objeto e passando valores para os atributos
objeto.metodo_filho() # executando o metodo da classe filha