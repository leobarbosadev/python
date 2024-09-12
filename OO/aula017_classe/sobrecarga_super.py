class ClassePai:  # Super Classe
    # Método construtor
    def __init__(self, a, b):
        self.a = a
        self.b = b

    # Método que vai ser sobrecarregado
    def metodo_classe(self):
        print('Aqui vou multiplicar a e b!')
        resultado = self.a * self.b
        print(f'Este calculo esta sendo realizado')
        print(f'pelo Metodo de Classe Pai!')
        print(
            f'O resultado da multiplicacao de {self.a} e {self.b} = {resultado}')


class ClasseFilha(ClassePai):  # Classe Derivada
    # Método construtor
    def __init__(self, a, b):
        super().__init__(a, b)  # Chama o construtor da classe pai
        # não é necessário redefinir a variável self.a e self.b,
        # pois ja foram iniciaizados pelo construtor da classe pai

    # Sobrecarga de Metodo
    def metodo_classe(self):
        # Primeiro, executa o metodo da classe pai
        super().metodo_classe()
        # Depois, executa o metodo da classe filha
        resultado = self.a + self.b
        print(f'O resultado da soma na Classe Filha é: {resultado}')


# Programa principal
teste = ClasseFilha(1, 2)
teste.metodo_classe()
