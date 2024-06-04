#Faça um programa que leia o nome de uma pessoa e verifique se a palavra 'Oliveira' está presente neste nome, mostrando True ou False.

import os


os.system('cls')

nome = input('Entre com seu nome: ').lower() # JÁ FAÇO A CONVERSÃO PARA MINÚSCULO

print(f'Texto: {nome.title()}')

# if 'Oliveira' in nome:
#     print(bool('Oliveira'))
# else:
#     print(bool())

retorno = 'oliveira' in nome

if retorno == True:
    print(f'{retorno} Verdadeiro')
else:
    print(f'{retorno} Falso')