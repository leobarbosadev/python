# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Leonardo Barbosa
# Data:
# Crie uma função que receba 2 listas:
# - lista 1: nome, peso, idade
# - lista 2: John, 40, 1.8
# - Sua função deverá criar um dicionário contendo chave e valor utilizando como
# base essas duas listas. Depois, seu programa deverá imprimir esse dicionário
# utilizando uma estrutura de repetição for.
import os


os.system('cls')

lista_1 = ['nome', 'peso', 'idade']
lista_2 = ['John', 40, 1.8]


def receber_listas():

    dicionario = dict(zip(lista_1, lista_2))

    for chave, valor in dicionario.items():
        print(f'{chave}: {valor}')

receber_listas()
print()
