#Faça um programa que leia o nome de uma pessoa e verifique se a palavra 'Oliveira' está presente neste nome, mostrando True ou False.

import os


os.system('cls')

nome = input('Entre com seu nome: ')

print(f'Texto: {nome}')
if 'Oliveira' in nome:
    print(bool('Oliveira'))
else:
    print(bool())