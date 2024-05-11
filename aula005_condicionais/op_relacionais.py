# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Leonardo Barbosa
# Data: 25/04/2024
# Operadores Relacionais

import os


os.system('cls')

a = input('Escreva um número: ')
b = input('Escreva um número: ')
c = input('Escreva uma palavra: ')
d = input('Escreva uma palavra: ')

print('-' * 70)
print('Condicionais: Operadores Relacionais')
('=' * 70)

# Igualdade (==)
if c == d:
    print('-' * 70)
    print(f'{c} é igual a {d}')
    print('=' * 70)
else:
    print(f'{c} não é igual a {d}')

# Diferença (!=)
if a != c:
    print('=' * 70)
    print(f'{a} é diferente de {c}')
    print('=' * 70)
else:
    print(f'{a} não é diferente de {c}')

# Maior que (>)
if a > b:
    print('-' * 70)
    print(f'{a} é maior que {b}')
    print('=' * 70)
else:
    print(f'{a} não é maior que {b}')

# Menor que(<)
if b < a:
    print('-' * 70)
    print(f'{b} é menor que {a}')
    print('=' * 70)
else:
    print(f'{b} não é menor que {a}')

# Maior ou igual a (>=)
if a >= b:
    print('-' * 70)
    print(f'{a} é maior ou igual a {b}')
    print('=' * 70)
else:
    print(f'{a} não é maior ou igual a {b}')

# Menor ou igual a(<=)
if b <= a:
    print('-' * 70)
    print(f'{b} é menor ou igual a {a}')
    print('=' * 70)
else:
    print(f'{b} não é menor ou igual a {a}')
    
print('Fim do programa!')
print('-' * 70)
print()