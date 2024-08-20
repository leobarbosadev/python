# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Leonardo Barbosa
# Data: 01/07/2024
# d) Faça um programa para criar um dicionário com 5  cores. Depois,  imprima as # chaves e os valores deste dicionário.
import os


os.system('cls')

print('-' * 70)
print('ADICIONAR E EXIBIR CORES')
print('=' * 70)

cores = {}
for c in range(5):
    print(f'Adicionando a {c + 1}ª cor:')
    print()
    chave = input('Entre com a chave: ')
    valor = input('Entre com o valor: ')
    print()
    cores[chave] = valor

print('DICIONÁRIO DE CORES:')
for chave, valor in cores.items():
    print(f'{chave.capitalize()}: {valor.capitalize()}')
print()
