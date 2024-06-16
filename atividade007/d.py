# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Leonardo Barbosa
# Data: 17/06/2024
# d)Utilizando o exercício anterior, coloque todas as listas em ordem crescente de valor

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

for i in range(0, len(lista), 10):
    lista_fatiada.append(lista[i:i + 10])
print('Listas Fatiadas')
for indice, lista in enumerate(lista_fatiada, start=1):
  lista.sort()
  # lista_ordenada = sorted(lista)
  print(f'Lista ordenada {indice}: {lista}.')
  print()
