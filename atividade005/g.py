# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Leonardo Barbosa
# Data: 03/06/2024
# Faça um programa que calcule os números primos
# em um intervalo pré-determinado pelo usuário.

import os


os.system('cls')

print('-' * 80)
print('*** NÚMEROS PRIMOS ***')
print('=' * 80)

inicio = int(input('Entre com o início do intervalo: '))
fim = int(input('Entre com o final do intervalo.: '))

for c in range(inicio, fim + 1):
    contador = 0 # Quantidade de vezes que o número pode ser divido
    for c2 in range(1, fim + 1):
        if c % c2 == 0:
            contador += 1
    if contador == 2:
        print(c)
