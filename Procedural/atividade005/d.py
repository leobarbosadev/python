# Faça um programa que imprima os números pares entre 0 e 100.

import os


os.system('cls')

i = 0
for c in range(0, 101):
    par = c % 2 == 0
    if par == True:
        i += 1
        print(c, end=' | ')
print(f'\nQuantidade de pares: {i}')
print()
