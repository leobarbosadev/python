# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Leonardo Barbosa
# Data: 17/06/2024
# f)Faça um programa que recebe 7 números inteiros. Depois quebre essa lista em: lista de pares e lista de ímpares.

import os


os.system('cls')

os.system('cls')

print('-' * 80)
print('LISTA PARES E ÍMPARES')
print('=' * 80)

lista = []
lista_pares = []
lista_impares = []

while len(lista) <= 6: # PARA CRIAR UMA LISTA COM 7 NÚMEROS, DEFINO O TAMANHO COMO 7 (DE 0 A 6)
    entrada = int(input('Entre com um número: '))
    lista.append(entrada)

for i in range(1, len(lista)):
  if i % 2 == 0:
    lista_pares.append(i)
  else:
    lista_impares.append(i)
    
print(f'Lista de números pares: {lista_pares}')
print(f'Lista de números ímpares: {lista_impares}')
