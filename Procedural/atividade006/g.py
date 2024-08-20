# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Leonardo Barbosa
# Data: 17/06/2024
# g)Ler uma lista com 10 números, depois apresente o maior e o menor número da lista

import os


os.system('cls')

print('-' * 80)
print('MAIOR E MENOR NÚMERO EM UMA LISTA')
print('=' * 80)

lista_numeros = []

for i in range(0, 10):
    numeros = int(input('Entre com um número: '))
    lista_numeros.append(numeros)

print()
print(f'Lista digitada: {lista_numeros}')

lista_numeros.sort()
menor = lista_numeros[0]
maior = lista_numeros[-1]

print(f'Menor número da lista: {menor}')
print(f'Maior número da lista: {maior}')
print()
