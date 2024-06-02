# Faça um programa que imprima os números primos entre 0 e 100.
# 2, 3, 5, 7, 11, 13, 17 e 19
import os


os.system('cls')

numero = 3
for c in range(0, 20):
    if c < 2:
        continue
    elif (c % numero != 0):
        print(c)
        
