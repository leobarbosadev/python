# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Leonardo Barbosa
# Data: 17/06/2024
# b)Crie uma lista com 5 números inteiros. Depois imprima a soma desses valores.

import os


os.system('cls')

print('-' * 80)
print('CRIAR E IMPRIMIR NÚMEROS')
print('=' * 80)

lista = []
soma = 0

for i in range(0,5):
  numeros = int(input('Entre com um número inteiro: '))
  lista.append(numeros)
  soma += numeros
  
print('-' * 80)
print(f'Os números digitados foram: {lista} e a soma deles é: {soma}')
print()