# Faça um programa que imprima os números no intervalo entre 1 e 10 em ordem inversa.

import os

# class Apresentar:
#     def __init__(self, inicio, fim):
#         self.inicio = inicio
#         self.fim = fim


# class Intervalo(Apresentar):
#     def exibir_numeros(self):
#         for c in range(10, 0, -1):
#             print(f'Contador {c}')

class Apresentar: # superclasse ou classe pai
    def __init__(self, inicio, fim):
        self.inicio = inicio
        self.fim = fim

    def exibir_numeros(self, inicio, fim):
        print('Não vai imprimir nada') # Vai ser sobrecarregado, para mostrar na tela, tenho que usar o super


class Intervalo(Apresentar): # subclasse ou classe classe derivada
    def __init__(self, inicio, fim):
        self.inicio = inicio
        self.fim = fim

    def exibir_numeros(self):
        for c in range(10, 0, -1):
            print(f'{c}', end=' | ')


os.system('cls')
print('CONTAGEM REGRESSIVA')
intervalo = Intervalo(1, 10)
intervalo.exibir_numeros()
