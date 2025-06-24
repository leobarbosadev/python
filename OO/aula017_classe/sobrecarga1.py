class ClassePai:  # Super Classe
    # Método construtor
    def __init__(self, a, b):
        self.a = a
        self.b = b

    # Para sobrecarregar
    # Vai ser usada para somar 2 numeros
    def metodo_classe(self, a, b):
        pass


class ClasseFilha(ClassePai):  # Classe Derivada
    # Método construtor
    def __init__(self, a, b):
        self.a = a
        self.b = b

    # Sborecarga de Metodo
    def metodo_classe(self):
        return self.a + self.b


# Programa principal
teste = ClasseFilha(1, 2)
exibe = teste.metodo_classe()
print(exibe)
