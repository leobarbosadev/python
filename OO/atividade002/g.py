# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Leonardo Barbosa
# Data: 03/06/2024
# Faça um programa que calcule os números primos
# em um intervalo pré-determinado pelo usuário.
import os


# class Numeros:
#     def __init__(self, inicio, fim):
#         self.inicio = inicio
#         self.fim = fim

#     def imprime(quantidade):
#         print(f'\nOs numeros primos entre: {quantidade}')


# class Primos(Numeros):
#     def mostra_primos(self):
#         for c in range(inicio, final + 1):
#             contador = 0  # QUANTAS VEZES O NÚMERO C É DIVIDIDO
#             for c2 in range(1, final + 1):
#                 if c % c2 == 0:
#                     contador += 1
#             if contador == 2:
#                 print(f'{c}', end=' | ')
#         Numeros.imprime(f'{self.inicio} e {self.fim} é: {c}')

class Numeros: # superclasse ou classe pai
    def __init__(self, inicio, fim):
        self.inicio = inicio
        self.fim = fim

    def mostrar_primos(self, inicio, fim):
        print('Não vai imprimir nada') # Vai ser sobrecarregado, para mostrar na tela, tenho que usar o super


class Primos(Numeros): # subclasse ou classe classe derivada
    def __init__(self, inicio, fim):
        self.inicio = inicio
        self.fim = fim
        
    def mostra_primos(self):
        for c in range(self.inicio, (self.fim + 1)):
            contador = 0  # QUANTAS VEZES O NÚMERO C É DIVIDIDO
            for c2 in range(1, self.fim + 1):
                if c % c2 == 0:
                    contador += 1
            if contador == 2:
                print(f'{c}', end=' | ')
        print()
        

os.system('cls')

inicio = int(input('Entre com o inicio do intervalo: '))
final = int(input('Entre com o final do intervalo..: '))
exibir_primos = Primos(inicio, final)
exibir_primos.mostra_primos()
