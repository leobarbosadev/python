# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Leonardo Barbosa
# Data: 01/07/2024
#i) Faça um programa para criar um dicionário com 4 elementos.
# Depois imprima a lista completa,
# delete o último elemento e mostre uma listagem nova.
import os


os.system('cls')

caracteristicas = {}
lista_caracteristica = []
quantidade = input('Quantos itens deseja adicionar? ')
quantidade = int(quantidade)

# CONTAGEM
for c in range(quantidade):
    print('-' * 70)
    print('DICIONÁRIO 4 ELEMENTOS')
    print('=' * 70)
    print(f'Adicionando o {c + 1}º elemento')
    caracteristicas['nome'] = input('Digite o nome..: ')
    caracteristicas['idade'] = input('Digite a idade.: ')
    caracteristicas['peso'] = input('Digite o peso..: ')
    caracteristicas['altura'] = input('Digite a altura: ')
    os.system('cls')
    
    lista_caracteristica.append(caracteristicas.copy())
    
print('-' * 70)
print('LISTA COM TODOS OS ITENS CADASTRADOS')
print('=' * 70)

for elemento in lista_caracteristica: # PARA CADA ELEMENTO NA LISTA
    for chave, valor in elemento.items():
        print(f'{chave.capitalize()}:{valor.capitalize()}', end=' | ')
    print()
print()

print('O último elemento será excluído')
lista_caracteristica.pop()

print('-' * 70)
print('LISTAGEM COM O ÚLTIMO ELEMENTO EXCLUÍDO')
print('=' * 70)
for elemento in lista_caracteristica:
    for chave, valor in elemento.items():
        print(f'{chave}: {valor}', end=' | ')
    print()
print()
