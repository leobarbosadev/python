# Faça um programa que imprima os números no intervalo entre 1 e 100.
# Os números devem ser apresentados na horizontal.
import os


# class Intervalo:
#     def __init__(self, inicio, fim):
#         self.inicio = inicio
#         self.fim = fim


# class ExibirIntervaloEntreNumeros(Intervalo):
#     def exibir(self):
#         for c in range(self.inicio, self.fim):  # for c in range(0, 100)
#             print(f'{c}', end=' | ')  # print(f'{c + 1}', end=',')

class Intervalo:  # superclasse ou classe pai
    def __init__(self, inicio, fim):
        self.inicio = inicio
        self.fim = fim

    def exibir(self, inicio, fim):
        print('Não vai printar nada') # Vai ser sobrecarregado, para mostrar na tela, tenho que usar o super


class ExibirIntervaloEntreNumeros(Intervalo): # subclasse ou classe classe derivada
    def __init__(self, inicio, fim):
        self.inicio = inicio
        self.fim = fim

    def exibir(self):
        for c in range(1, 101):
            print(f'{c}', end=' | ')  # print(f'{c + 1}', end=',')


os.system('cls')

print('-' * 80)
print('*** DE 1 ATÉ 100 ***')
# intervalo = ExibirIntervaloEntreNumeros(1, 100)
intervalo = ExibirIntervaloEntreNumeros(1, 101)
# QUANDO TEMOS UM PRINT DENTO DO METODO, NÃO PRECISO ATRIBUIR O METODO A UMA VARIAVEL.
intervalo.exibir()
print()
print('=' * 80)
print()
