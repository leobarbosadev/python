#Faça um programa que receba o nome completo de uma pessoa e, posteriormente, imprima esse nome separadamente.

import os


os.system('cls')

nome = input('Entre com o nome completo: ')
nome_separado = nome.split() # Colocar o separador que vai ser usado na frase, ex: espaço ou vírgula

print(f'O nome separado é: {nome_separado}')