# Faça um programa que imprima os números pares entre 0 e 100.

import os

# class Numeros:
#     def __init__(self, inicio, fim):
#         self.inicio = inicio
#         self.fim = fim


# class ExibirPares(Numeros): # subclasse ou classe classe derivada
#     def exibir(self):
#         for c in range(0, 101):
#             par = c % 2 == 0
#             if par == True:
#                 print(c, end=' | ')

class Numeros: # superclasse ou classe pai
    def __init__(self, inicio, fim):
        self.inicio = inicio
        self.fim = fim

    def exibir(self, inicio, fim):
        print('Não vai imprimir nada') # Vai ser sobrecarregado, para mostrar na tela, tenho que usar o super


class ExibirPares(Numeros): # subclasse ou classe classe derivada
    def __init__(self, inicio, fim):
        self.inicio = inicio
        self.fim = fim

    def exibir(self):

        for c in range(0, 101):
            par = c % 2 == 0
            if par == True:
                print(c, end=' | ')


os.system('cls')
print('PARES DE 0 A 100')
exibe_pares = ExibirPares(0, 100)
exibe_pares.exibir()
