# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Leonardo Barbosa
# Data: 01/07/2024
#j) Faça um programa para criar um dicionário com nomes de frutas.
# Em seguida verifique se tem abacaxi nos valores.
import os


os.system('cls')

print('-' * 70)
print('ADICIONANDO FRUTAS')
print('=' * 70)

fruta = 'Abacaxi'
frutas = {}
quantidade_itens = input('Quantos itens deseja adicionar? ')
print()
quantidade_itens = int(quantidade_itens)

for c in range(quantidade_itens):
    print(f'Adicionando o {c + 1}º item:')
    chave = input('Insira a chave: ')
    valor = input('Insira o valor: ')
    frutas[chave] = valor
    print()
    
if fruta in frutas:
    print(f'{fruta} foi encontrado')
else:
    print(f'{fruta} não foi encontrado')