class ClassePai:  # criação da classe pai
    def __init__(self, a, b):  # metodo construtor
        # iniciar os atributos
        self.a = a
        self.b = b


class ClasseFilha(ClassePai):  # classe filha herda de classe pai
    def __init__(self, a, b):  # metodo construtor da super classe
        # iniciar os atributos
        self.a = a
        self.b = b

    def metodo_classe_filha(self): # metodo da classe filha
        print('Soma')
        soma = self.a + self.b
        print(f'A soma de {self.a} + {self.b} = {soma}')


exibe = ClasseFilha(1, 2) # instanciando o objeto
exibe.metodo_classe_filha() # executando o metodo da classe filha
