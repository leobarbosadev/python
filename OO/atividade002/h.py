# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Leonardo Barbosa
# Data: 03/06/2024
# Faça um programa que imprima os valores no intervalo definidos pelo usuário.
# Defina 3 números que deverão ser ignorados,
# ou seja, que não serão impressos na tela.
import os

# class Numeros:
#     def __init__(self, inicio, final):
#         self.inicio = inicio
#         self.fim = final

#     def exibir_titulo():
#         print('-' * 80)
#         print('*** EXCLUIR TRÊS NÚMEROS ***')
#         print('=' * 80)
#         print()

#     def exibir_excluidos():
#         print('-' * 80)
#         print('NÚMEROS PARA SEREM EXCLUÍDOS')
#         print('-' * 80)


# class ExcluirNumeros(Numeros):
#     def excluir(self):
#         for c in range(inicio, fim):
#             if c == numero_1 or c == numero_2 or c == numero_3:
#                 continue
#             print(c, end=' | ')

class Numeros: # superclasse ou classe pai
    def __init__(self, inicio, final, numero_1, numero_2, numero_3):
        self.inicio = inicio
        self.fim = final
        self.numero_1 = numero_1
        self.numero_2 = numero_2
        self.numero_3 = numero_3

    def excluir(self, inicio, final, numero_1, numero_2, numero_3):
        print('Não vai imprimir nada') # Vai ser sobrecarregado, para mostrar na tela, tenho que usar o super


class ExcluirNumeros(Numeros): # subclasse ou classe classe derivada
    def __init__(self, inicio, final, numero_1, numero_2, numero_3):
        self.inicio = inicio
        self.fim = final
        self.numero_1 = numero_1
        self.numero_2 = numero_2
        self.numero_3 = numero_3

    def excluir(self):
        for c in range(inicio, fim):
            if c == numero_1 or c == numero_2 or c == numero_3:
                continue
            print(c, end=' | ')


os.system('cls')

print('*** EXCLUIR TRÊS NÚMEROS ***')
inicio = int(input('Digite o início do intervalo...: '))
fim = int(input('Digite o fim do intervalo......: ')) + 1

print('NÚMEROS PARA SEREM EXCLUÍDOS')
numero_1 = int(input('Entre com o 1º número a ser excluído: '))
numero_2 = int(input('Entre com o 2º número a ser excluído: '))
numero_3 = int(input('Entre com o 3º número a ser excluído: '))

excluir = ExcluirNumeros(inicio, fim, numero_1, numero_2, numero_3)
print('Lista sem os numeros excuidos')
excluir.excluir()
print()
print('-' * 80)
print()
