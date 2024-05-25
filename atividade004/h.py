# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Leonardo Barbosa
# Data: 23/05/2024
#Faça um programa que leia o nome de um aluno e mostre quantas vezes a letra 'o' aparece e em que posição ela aparece pela primeira e última vez.

import os


os.system('cls')

nome = input('Entre com o nome do aluno: ').lower()

quantidade_o = nome.count('o')
primeira_vez = nome.find('o') + 1 # Vai retornar a posição e não o índice
ultima_vez = nome.rfind('o') + 1

print(f'A quantide de "o" é: {quantidade_o}, '
      + f'a primeira vez que aparece a letra o é na posição {primeira_vez},'
      + f'a ultima vez é {ultima_vez}')
