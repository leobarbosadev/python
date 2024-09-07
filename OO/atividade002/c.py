# Faça um programa que imprima os números no intervalo entre 1 e 10 em ordem inversa.

import os


# VERIFICAR ESSE
class Apresentar:
    def __init__(self, inicio, fim):
        self.inicio = inicio
        self.fim = fim


class Intervalo(Apresentar):
    def exibir_numeros(self):
        for c in range(10, 0, -1):
            print(f'Contador {c}')


os.system('cls')
intervalo = Intervalo(1, 10)
intervalo.exibir_numeros()
