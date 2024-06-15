# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Leonardo Barbosa
# Data: 17/06/2024
# f)Faça um programa que leia 5 nomes, depois imprima estes nomes com seus respectivos índices.

import os


os.system('cls')

print('-' * 80)
print('NOMES E ÍNDICES')
print('=' * 80)

lista_nomes = []

for i in range(0,5):
  nomes = input('Entre com um nome:')
  lista_nomes.append(nomes)
print()

for indice, nome in enumerate(lista_nomes):
  print(f'Índice: {indice} = {nome}')
print()
