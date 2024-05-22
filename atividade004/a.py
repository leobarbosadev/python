# Faça um programa que solicite separadamente o nome, o nome do meio e o sobrenome de uma pessoa. Em seguida, imprima o nome completo.

import os


os.system('cls')

nome = input('Entre com seu nome: ')
nome_meio = input('Entre com o nome do meio: ')
sobrenome = input('Entre com o sobrenome: ')

lista = [nome , nome_meio, sobrenome]
juncao = " ".join(lista)
print(f'A junção das strings ficam: {juncao}')