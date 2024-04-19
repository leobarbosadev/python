# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Leonardo Barbosa
# Data: 19/04/2024
# Faça um programa que converta metros em centímetros e milímetros.

# imports
import os


os.system('cls')

print('-' * 70)
print('ENTRADA DE DADOS')
print('-' * 70)

# Entrada
metros = float(input('Digite quantos metros quer conveter: '))

# Processamento
centimetros = metros * 100
milimetros = metros * 1000

#Saída
print('-' * 70)
print('RESULTADO')
print('=' * 70)
print(f'{metros} m convertido para centímetros é: {centimetros} cm')
print(f'{metros} m convertido para milímetros é: {milimetros} mm')
print('-' * 70)
print()