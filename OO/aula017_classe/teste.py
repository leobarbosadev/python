class ClassePai:  # Super classe ou classe pai
    def __init__(self, a, b):  # método construtor (a e b são atributos)
        self.a = a
        self.b = b

    def metodo_classe_pai(self):
        print('Metodo da classe pai')


class ClasseFilha(ClassePai): # classe filha herda classe pai
    def __init__(self, a, b): # metodo construtor da super classe
        super().__init__(a, b) # acessa o método da classe pai

    def metodo_classe_pai(self): # metodo da classe pai herdado para filha
        return super().metodo_classe_pai()

mostrar = ClasseFilha(1, 2) # instanciando o objeto
mostrar.metodo_classe_pai() # executando o metodo da classe filha
