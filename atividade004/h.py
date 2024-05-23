# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Leonardo Barbosa
# Data: 23/05/2024
#Faça um programa que leia o nome de um aluno e mostre quantas vezes a letra 'o' aparece e em que posição ela aparece pela primeira e última vez.

import os


os.system('cls')

nome = input('Entre com o nome do aluno: ').lower()

primeira_vez = nome.find('o') + 1 # Vai retornar a posição e não o índice

ultima_posicao = len(nome) - nome[::-1].find('o')

print(f'A primeira vez que aparece a letra o é no índice {primeira_vez}')
print(f'A ultima vez é {ultima_posicao}')
