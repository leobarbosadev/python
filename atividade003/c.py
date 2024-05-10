#Faça um programa que receba as informações de base e expoente. Calcule a potência.

import os
import math


os.system('cls')

base = float(input('Entre com um valor para a base: '))
expoente = float(input('Entre com um valor para o expoente: '))

potenceia = math.pow(base, expoente)

print(f'A potenciação de {base} e expoente {expoente} é: {potenceia}')
