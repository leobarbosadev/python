# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Leonardo Barbosa
# Data: 01/07/2024
# a) Faça um programa para criar um dicionário com 4 elementos.
import os


os.system('cls')

print('-' * 70)
print('DICIONÁRIO COM 4 ELEMENTOS')
print('=' * 70)

cadastro = {}  # dict => {}

# cadastro['nome'] = 'Leonardo'
# cadastro['idade'] = 28
# cadastro['endereco'] = 'rua A'
# cadastro['cidade'] = 'Juiz de Fora'

quantidade_itens = input('Quantos itens deseja inserir? ')
quantidade_itens = int(quantidade_itens)

for c in range(quantidade_itens):
    print(f'Adicionando o elemento {c + 1}')
    print()
    chave = input('Entre com a chave: ')
    valor = input('Entre com o valor: ')
    cadastro[chave] = valor
    print()


for chave, valor in cadastro.items():
    print(f'{chave}: {valor}', end=', ')
print()
print()
