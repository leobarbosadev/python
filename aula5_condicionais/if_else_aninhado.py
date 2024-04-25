# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Leonardo Barbosa
# Data: 25/04/2024
# Verificando se un número é maior, menor ou igual

import os


os.system('cls')

# Declarações
a = input('Digite um número: ')
b = input('Digite outro número: ')
resposta = ''

print('-' * 70)
print('Estudo de Condicional (Aninhada)')
('=' * 70)

if a > b:
    resposta = f'{a} é maior que {b}'
elif a < b:
    resposta = f'{a} é menor que {b}'
else:
    resposta = f'Os valores são iguais: {a} = {b}'

# Saída
print('-' * 70)
print(resposta)
print('-' * 70)
print()