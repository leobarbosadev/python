# Faça um programa que imprima os números no intervalo entre 1 e 100.
# Os números devem ser apresentados na horizontal.

import os


os.system('cls')

print('-' * 80)
print('*** DE 1 ATÉ 100 ***')
print('=' * 80)
print()

for c in range(0, 100):
    print(f'{c + 1}', end=',') # COLOCO O + 1 PARA PODER COMEÇAR A CONTAR NO 1 E NÃO NO 0
print()
print()
    
