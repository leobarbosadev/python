# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Leonardo Barbosa
# Data: 04/09/2024
# Faça um programa com entrada de dados para calcular o perímetro de um retângulo.
import os


class Rentangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def perimetro(self):
        self.base = float(self.base)
        self.altura = float(self.altura)
        perimetro = 2 * (self.base + self.altura)
        return perimetro


os.system('cls')
base = input('Entre com o valor da base....: ')
altura = input('Entre com o valor da altura: ')
calculo = Rentangulo(base, altura)
calcular_perimetro = calculo.perimetro()
print(f'O perimetro do retangulo de base {base} e altura {altura} é {calcular_perimetro}')
