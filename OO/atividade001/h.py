# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Leonardo Barbosa
# Data: 03/09/2024
# Faça um programa que receba um número inteiro, depois imprima sua tabuada de multiplicação.
import os


class Tabuada:
    def __init__(self, valor):
        self.valor = valor

    def calcular_tabuada(self):
        self.valor = int(self.valor)
        for i in range(0, 11):
            resultado = self.valor * i
            print(f'{self.valor} x {i} = {resultado}', end='\n')


os.system('cls')
entrada = input('Entre com um valor para exibir sua tabuada: ')
tabuada = Tabuada(entrada)
print(f'---Tabuada do {entrada}---')
resultado = tabuada.calcular_tabuada()
print()
