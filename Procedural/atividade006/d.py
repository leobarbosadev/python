# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Leonardo Barbosa
# Data: 17/06/2024
#d)Faça um programa que preencha uma lista com as notas de 4 alunos, depois imprima a média.

import os


os.system('cls')

print('-' * 80)
print('MÉDIA DAS NOTAS')
print('=' * 80)

lista_notas = []
media = 0
soma = 0

for i in range(0,4):
  notas = float(input('Entre com uma nota: '))
  lista_notas.append(notas)
  soma += notas

media = soma / len(lista_notas)

print(f'As notas digitas foram: {lista_notas}, a média delas é: {media:.2f}')
print()


  