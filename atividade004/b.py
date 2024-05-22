#Faça um programa que receba o nome 'João da Silva' e, em seguida, substitua 'Silva' por 'Oliveira'.

import os


os.system('cls')

nome = 'João da Silva'

substituir = nome.replace('da Silva','de Oliveira')
print(f'Nome original: {nome}')
print(f'Nome novo: {substituir}')
print()