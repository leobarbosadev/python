# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Leonardo Barbosa
# Data: 03/09/2024
# Faça um programa que receba um número qualquer e calcule o dobro e o triplo desse número.
import os


class Calcular:
    def __init__(self, valor):
        self.valor = valor

    def dobro_e_triplo(self):
        # Usar try except para tratar erros e validar
        self.valor = float(self.valor)
        dobro = self.valor * 2
        triplo = self.valor * 3
        return dobro, triplo

os.system('cls')
valor = input('Entre com um valor par ver seu dobro e seu triplo: ')
calcular = Calcular(valor)
dobro, triplo = calcular.dobro_e_triplo()
print(f'O dobro de {valor} é {dobro} e o triplo é {triplo}')
