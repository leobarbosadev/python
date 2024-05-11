#Faça um programa para sortear um número de 1 a 20

import  os
import random


os.system('cls')

print('SORTEIO DE NÚMEROS')
print('=' * 70)
aleatorio = random.randint(1, 20)
print(f'O número sorteado foi: {aleatorio}')
print('-' * 70)
print()