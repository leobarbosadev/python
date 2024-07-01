# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Leonardo Barbosa
# Data: 01/07/2024
# k) Faça um programa que peça continuamente o nome e a idade de uma pessoa.
# Caso o usuário digite a idade 999, o programa será finalizado e
# executará uma impressão com os nomes cadastrados.
import os


os.system('cls')

pessoas = {}

print('-' * 70)
print('ADICIONANDO PESSOAS')
print('=' * 70)

while True:
    chave = input('Digite o nome..........................: ')
    valor = input('Digite a idade (999 - fecha o programa): ')
    pessoas[chave] = valor

    if valor == '999':
        os.system('cls')
        print('Todos as pessoas cadastradas: ')
        for chave, valor in pessoas.items():
            print(f'{chave}:{valor}')
        print()
        break
