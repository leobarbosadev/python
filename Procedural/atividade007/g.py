# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Leonardo Barbosa
# Data: 17/06/2024
#g) Faça um programa que gere 10 números aleatórios. Após gerar esses números, crie duas listas novas com ordenação ascendente e descendente.

import os
import random


os.system('cls')

print('-' * 80)
print('LISTA ASCENDENTE E DESCENDENTE')
print('=' * 80)

lista = []
lista_ascendente = []
lista_descendente = []

for i in range(0, 10):
  numeros_aleatorios = random.randint(1,10)
  lista.append(numeros_aleatorios)
lista_ascendente.extend(lista)# ESTOU ADICIONANDO OS ELEMENTOS DA LISTA EM LISTA ASCENDENTE E DESCENDENTE
lista_descendente.extend(lista)

lista_ascendente.sort()
lista_descendente.sort(reverse=True)

print(f'Lista: {lista}')
print()
print(f'Lista ascendente: {lista_ascendente}')
print()
print(f'Lista descendente: {lista_descendente}')
print()