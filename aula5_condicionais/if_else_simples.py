# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Leonardo Barbosa
# Data: 25/04/2024
# Verficando se um número é maior ou menor

import os


os.system('cls')

#Declarações
a = input('Digite um número: ')
b = input('Digite outro número: ')
resposta = ''

print('-' * 70)
print('Estudo de Condicional (Simples)')
('=' * 70)

#Condicionais
if a > b:
    resposta = f'{a} é maior que {b}'
else:
    resposta = f'{a} não é maior que {b}'
    
#Saída
print('-' * 70)
print(resposta)
print('-' * 70)
print()