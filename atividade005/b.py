#Evolua o programa anterior para um código que pergunte ao usuário qual o
# intervalo que ele deseja ver  impresso.

import os


os.system('cls')

print('-' * 80)
print('*** CONTAR ENTRE INTERVALOS DEFINIDOS PELO USUÁRIO ***')
print('=' * 80)
print()

inicio = int(input('Entre com um número inicial: '))
fim = (int(input('Entre com um número final: '))) + 1

for c in range(inicio, fim):
        print(f'{c}', end= ', ')
print()
