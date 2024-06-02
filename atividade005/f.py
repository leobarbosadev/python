# Faça um programa que imprima os números primos entre 0 e 100.

import os


os.system('cls')

for c in range(0, 101):
    contador = 0 # QUANTAS VEZES O NÚMERO C É DIVIDIDO
    for c2 in range(1,100):
        if c % c2 == 0:
            contador += 1

    if contador == 2:
        print(c, end= ' | ')


