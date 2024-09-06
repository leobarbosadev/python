# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Leonardo Barbosa
# Data: 03/06/2024
# Faça um programa que calcule os números primos
# em um intervalo pré-determinado pelo usuário.

import os


os.system('cls')

print('-' * 80)
print('*** NÚMEROS PRIMOS COM ENTRADA DE DADOS ***')
print('=' * 80)
print()

inicio = int(input('Entre com o início do intervalo: '))
fim = int(input('Entre com o final do intervalo.: '))
print()

for c in range(inicio, fim + 1):
    contador = 0  # Quantidade de vezes que o número pode ser divido
    for c2 in range(1, fim + 1):
        if c % c2 == 0:
            contador += 1
    if contador == 2:  # Todo número primo só pode ser divido 2 vezes.
        print(c, end=' | ')
print()
print()