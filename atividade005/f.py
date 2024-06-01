# Faça um programa que imprima os números primos entre 0 e 100.
# 2, 3, 5, 7, 11, 13, 17 e 19
import os


os.system('cls')

numero = 2
for c in range(0, 20):
    if c % numero != 0:
        # numero = numero + c
        print(c)
