# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Leonardo Barbosa
# Data: 23/05/2024
#Faça um programa que receba o nome completo de uma pessoa e, em seguida, mostre 
#o primeiro e o último nome.

import os


os.system('cls')

nome = input('Entre com o nome completo: ')

nome_lista = nome.split() # divide o nome em uma lista
primeiro_nome = nome_lista[0]
ultimo_nome = nome_lista[-1]

print(f'O nome digitado foi: {nome}\n'
      + f'O primeiro nome é: {primeiro_nome}\n'
      + f'O último nome é: {ultimo_nome}')


