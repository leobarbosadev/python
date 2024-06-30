# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Leonardo Barbosa
# Data: 01/07/2024
# e) Faça um programa para criar um dicionário com 5  ferramentas. Depois,
# imprima os valores e a quantidade de elementos do dicionário.
import os


os.system('cls')

print('-' * 70)
print('DICIONÁRIO DE FERRAMENTAS')
print('=' * 70)

ferramentas = {}

# CONTAGEM
for c in range(5):
    print(f'Adicionando {c + 1}ª ferramenta')
    print()
    chave = input('Entre com a chave: ')
    valor = input('Entre com o valor: ')
    print()
    # ADICIONA AS ENTRADAS DIGITAS ACIMA NO DICIONÁRIO
    ferramentas[chave] = valor

print('Elementos: ')
# VARREDURA
for chave, valor in ferramentas.items():
    print(f'{chave.capitalize()}:{valor}', end=' | ')
print()

quantidade_elementos = len(ferramentas)

print(f'Quantidade de elementos: {quantidade_elementos}')
print()
