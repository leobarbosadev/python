# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Leonardo Barbosa
# Data: 29/04/2024
# F) A empresa "LeapYearCheck" está desenvolvendo um software de verificação de anos bissextos para auxiliar
# usuários na identificação desses anos de forma rápida e precisa. 
# Eles precisam de um programa que permita aos usuários inserir um ano e, em seguida, 
# determine se esse ano é bissexto ou não, de acordo com as regras estabelecidas pelo calendário gregoriano. 
# Além disso, é necessário realizar a validação de entrada de dados para garantir que o ano inserido pelo usuário seja um valor válido,
# ou seja, um número inteiro positivo.

import os


os.system('cls')

print('-' * 80)
print('Ano Bissexto')
print('-' * 80)

#Entrada
ano = int(input('Entre com um ano: '))
resposta = ''

#Condicional
if ano % 4 == 0:
    resposta = f'O ano digitado foi {ano}, ele é bissexto'
else:
    resposta = f'O ano digitado foi {ano}, ele não é bissexto'
    
#Saída
print('-' * 80)
print(resposta)
print()