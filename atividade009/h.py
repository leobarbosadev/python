# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Leonardo Barbosa
# Data: 01/07/2024
#h) Faça um programa para ler o dicionário 
# nomes = {‘nome’: ’John, ‘idade’: 40,‘peso’: 80, ‘altura’: 1.70}.
# Em seguida realize as seguintes ações:
# - Listar chaves e valores com laço - Deletar o peso
# - Listar novamente chaves e valores - mostrar o nome e altura
import os


os.system('cls')

print('-' * 70)
print('DICIONÁRIO NOME, IDADE, PESO, ALTURA')
print('=' * 70)

nomes = {'nome': 'John', 'idade': 40, 'peso': 80, 'altura': 1.70}

if nomes:
    print(f'Itens do dicionário: {nomes.items()}')