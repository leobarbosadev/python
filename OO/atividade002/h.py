# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Leonardo Barbosa
# Data: 03/06/2024
#Faça um programa que imprima os valores no intervalo definidos pelo usuário.  
# Defina 3 números que deverão ser ignorados, 
# ou seja, que não serão impressos na tela.

import os


os.system('cls')

print('-' * 80)
print('*** EXCLUIR TRÊS NÚMEROS ***')
print('=' * 80)
print()

inicio = int(input('Digite o início do intervalo...: '))
fim = int(input('Digite o fim do intervalo......: ')) + 1
print('-' * 80)
print('NÚMEROS PARA SEREM EXCLUÍDOS')
print('-' * 80)
numero_1 = int(input('Entre com o 1º número a ser excluído: '))
numero_2 = int(input('Entre com o 2º número a ser excluído: '))
numero_3 = int(input('Entre com o 3º número a ser excluído: '))

print()


for c in range(inicio, fim):
    if c == numero_1 or c == numero_2 or c == numero_3:
        continue
    print(f'O número é {c}')
print('-' * 80)
print()
