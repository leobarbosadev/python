# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Leonardo Barbosa
# Data: 17/06/2024
# c)Faça um programa que preencha uma lista com 50 números aleatórios. Depois fatie essa lista em 5 listas de 10 elementos.

import os
import random

os.system('cls')

lista = []
lista_fatiada = []

for i in range(1, 51):
    numeros_aletatorios = random.randint(1, 50)
    lista.append(numeros_aletatorios)

print(f'Lista gerada: {lista}')
print()

for i in range(0, len(lista),10):
    lista_fatiada.append(lista[i:i + 10])
print('Listas Fatiadas')
for indice, lista in enumerate(lista_fatiada, start= 1):
    print(f'Lista {indice}: {lista}')
    print()
