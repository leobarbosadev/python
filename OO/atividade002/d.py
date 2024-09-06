#Faça um programa que imprima os números pares entre 0 e 100.

import os


os.system('cls')

for c in range(0, 101):
    numero = int(c + 1)
    par = numero % 2 == 0
    
    if par == True:
        print(numero, end=', ')
print()