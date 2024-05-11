# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Leonardo Barbosa
# Data: 19/04/2024
# Faça um programa que peça 4 notas, após a entrada de dados calcular a média das notas digitadas.

#imports
import os


os.system('cls')

print('-' * 70)
print('ENTRADA DE DADOS')
print('-' * 70)

#Entrada
nota1 = float(input('Entre com a 1ª nota: '))
nota2 = float(input('Entre com a 2ª nota: '))
nota3 = float(input('Entre com a 3ª nota: '))
nota4 = float(input('Entre com a 4ª nota: '))

#Processamento
soma = nota1 + nota2 + nota3 + nota4
media = soma / 4 # (nota1 + nota2 + nota3 + nota4) / 4

#Saída
print('-' * 70)
print('RESULTADO')
print('=' * 70)
print(f'Sua média é: {media}')
print('-' * 70)
print()
