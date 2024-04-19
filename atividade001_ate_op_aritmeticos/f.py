# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Leonardo Barbosa
# Data: 19/04/2024
# Faça um programa que receba um número qualquer e calcule o dobro e o triplo desse número.

#imports
import os


os.system('cls')

#Entrada
valor = float(input('Entre com um número: '))

#Processamento
dobro = valor * 2
triplo = valor * 3

#Saída
print('-' * 70)
print('RESULTADO')
print('=' * 70)
print(f'O número digitado foi: {valor} seu dobro é {dobro} e seu triplo é {triplo}')
print('-' * 70)
print()