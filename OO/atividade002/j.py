# Crie um programa que realiza a contagem de 1 até 100, usando apenas de números ímpares, ao final do processo exiba na
# tela quantos números ímpares foram encontrados nesse intervalo, assim como a soma dos mesmos.

import os


# class Numeros:
#     def __init__(self, inicio=1, fim=100):
#         self.inicio = inicio
#         self.fim = fim

#     def exibir_quantidade(valores):
#         print(f'\nA quantidade de números impares de  a 100 é: {valores}')

#     def exibir_soma(soma):
#         print(f'A soma dos números impares de  a 100 é: {soma}')

# class MostrarImpar(Numeros):
#     def exibir_impares(self):
#         quantidade_impar = 0
#         c = 0
#         soma = 0
#         for c in range(self.inicio, self.fim):
#             impar = c % 2 != 0
#             if impar == True:
#                 quantidade_impar += 1
#                 soma += c
#                 print(c, end=' | ')

#         Numeros.exibir_quantidade(quantidade_impar)
#         Numeros.exibir_soma(soma)

class Numeros:
    def __init__(self, inicio, fim):
        self.inicio = inicio
        self.fim = fim

    def mostrar(self, inicio, fim):
        # Vai ser sobrecarregado, para mostrar na tela, tenho que usar o super
        print('Não vai imprimir nada')


class MostrarImpar(Numeros):
    def __init__(self, inicio=1, fim=100):
        self.inicio = inicio
        self.fim = fim

    def mostrar(self):
        quantidade_impar = 0
        c = 0
        soma = 0
        for c in range(self.inicio, self.fim):
            impar = c % 2 != 0
            if impar == True:
                quantidade_impar += 1
                soma += c
                print(c, end=' | ')
        print()
        print(f'\nA soma dos numeros impares entre 1 e 100 é: {soma} '
              + f'\nA quantidade de numeros impares entre 1 e 100 é: {quantidade_impar}')


os.system('cls')
exibir_impar = MostrarImpar(1, 100)
exibir_impar.mostrar()
print()
