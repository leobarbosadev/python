# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Leonardo Barbosa
# Data: 01/07/2024
# f) Faça um programa que cadastra 5 tipos de vinho. Para os campos deste
# cadastro tome como referência nome do vinho, tipo, teor alcoólico e safra.
import os


os.system('cls')

print('-' * 70)
print('DICIONÁRIO DE VINHOS')
print('=' * 70)

vinhos = {}
lista_vinhos = []

# CONTAGEM
for c in range(5):
    print(f'Entre com o {c + 1}º vinho: ')
    vinhos['nome'] = input('Entre com o nome.........: ')
    vinhos['tipo'] = input('Entre com o tipo.........: ')
    vinhos['teor'] = input('Entre com o teor alcólico: ')
    vinhos['safra'] = input('Entre com a safra........: ')
    print()
    
    # USO O append() E O copy() PARA ADICIONAR UMA CÓPIA DO DICIONÁRIO NA LISTA
    lista_vinhos.append(vinhos.copy())

print('Vinhos:')
for elemento in lista_vinhos:  # PARA CADA ELEMENTO NA LISTA
    for chave, valor in elemento.items():  # PARA CADA CHAVE E VALOR DO DICIONÁRIO
        print(f'{chave.capitalize()}:{valor.capitalize()}', end=' | ')
    print()
