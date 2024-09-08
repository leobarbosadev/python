# Faça um programa que imprima os números pares entre 0 e 100.

import os


class Numeros:
    def __init__(self, inicio, fim):
        self.inicio = inicio
        self.fim = fim


class ExibirPares(Numeros):  # subclasse ou classe classe derivada
    def exibir(self):
        for c in range(0, 101):
            par = c % 2 == 0
            if par == True:
                print(c, end=' | ')


os.system('cls')

exibe_pares = ExibirPares(0, 100)
exibe_pares.exibir()
