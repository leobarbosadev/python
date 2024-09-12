class ClassePai: # Super Classe
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
        print(f'O resultado da multiplicacao de {self.a} e {self.b}')