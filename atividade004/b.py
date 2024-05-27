# Faça um programa que receba o nome 'João da Silva' e, em seguida, substitua 'Silva' por 'Oliveira'.

import os


os.system('cls')

nome = input('Entre com seu nome: ').lower()


# Validação
if not (nome.replace(' ', '').isalpha()):
    print('Contém caracter inválido!!!')
if 'silva' in nome:
    # lista = nome.split(' ')
    substituir = nome.replace('silva', 'Oliveira')
    print(f'Nome original: {nome.title()}')
    print(f'Nome novo: {substituir.title()}') # O MÉTODO .title() DEIXA A PRIMEIRA LETRA DE CADA PALAVRA EM MAÍSUCULA
else:
    print('Não foi encontrado Silva no seu nome')
