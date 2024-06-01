# Faça um programa que some a quantidade de números pares encontrados no intervalo entre 0 e 100.

import os


os.system('cls')

soma = 0

for c in range(0, 100):
    numero = int(c + 1)
    par = numero % 2 == 0 # RETORNA True e False
    # print(numero)
    # print(par)
    if par == True:
        print(numero, end=' | ')
        print(c)
