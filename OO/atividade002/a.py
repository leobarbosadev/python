# Faça um programa que imprima os números no intervalo entre 1 e 100.
# Os números devem ser apresentados na horizontal.
import os


class Intervalo:
    def __init__(self, inicio, fim):
        self.inicio = inicio
        self.fim = fim


class ExibirIntervaloEntreNumeros(Intervalo):
    def exibir(self):
        for c in range(self.inicio, self.fim):  # for c in range(0, 100)
            print(f'{c}', end=',')  # print(f'{c + 1}', end=',')


os.system('cls')

print('-' * 80)
print('*** DE 1 ATÉ 100 ***')
intervalo = ExibirIntervaloEntreNumeros(1, 101) # intervalo = ExibirIntervaloEntreNumeros(1, 100)
exibir_intervalo = intervalo.exibir()
print()
print('=' * 80)
print()
