# Faça um programa que imprima os números pares entre 0 e 100.

import os


class Numeros:
    def __init__(self, inicio, fim):
        self.inicio = inicio
        self.fim = fim


class ExibirPares(Numeros):  # subclasse ou classe classe derivada
    def exibir(self):
        i = 0
        for c in range(0, 101):
            par = c % 2 == 0
            if par == True:
                i += 1
                print(c, end=' | ')
        print(f'\nA quantidade de pares é: {i}')


os.system('cls')

exibe_pares = ExibirPares(0, 100)
exibe_pares.exibir()
