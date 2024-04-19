# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Leonardo Barbosa
# Data: 19/04/2024
# Faça um programa que receba um número inteiro e mostre o sucessor e antecessor.

# imports
import os


os.system('cls')

print('-' * 70)
print('ENTRADA DE DADOS')
print('-' * 70)

# Entada
valor = int(input('Entre com um número inteiro qualquer: '))

# Processamento
antecessor = valor - 1
sucessor = valor + 1

#Saída
print('-' * 70)
print('RESULTADO')
print('=' * 70)
print(f'O valor digitado foi {valor}, seu antecessor é {antecessor} e seu sucessor é {sucessor}')
print('-' * 70)
print()
