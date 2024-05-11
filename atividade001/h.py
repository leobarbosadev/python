# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Leonardo Barbosa
# Data: 19/04/2024
# Faça um programa que receba um número inteiro, depois imprima sua tabuada de multiplicação.

# imports
import os


os.system('cls')

print('-' * 70)
print('ENTRADA DE DADOS')
print('-' * 70)

# Entrada
numero = int(input('Digite um número inteiro: '))

#COM UM FOR É MAIS EFICAZ
# Processamento
valor1 = numero * 1
valor2 = numero * 2
valor3 = numero * 3
valor4 = numero * 4
valor5 = numero * 5
valor6 = numero * 6
valor7 = numero * 7
valor8 = numero * 8
valor9 = numero * 9
valor10 = numero * 10

# Saída
print('-' * 70)
print(f'O Resultado da tabuada do {numero} é:')
print('=' * 70)
print(f'{numero} x 1 = {valor1} \n{numero} x 2 = {valor2}\n'
      + f'{numero} x 3 = {valor3} \n{numero} x 4 = {valor4}\n'
      + f'{numero} x 5 = {valor5} \n{numero} x 6 = {valor6}\n'
      + f'{numero} x 7 = {valor7} \n{numero} x 8 = {valor8}\n'
      + f'{numero} x 9 = {valor9} \n{numero} x 10 = {valor10}')
print()




