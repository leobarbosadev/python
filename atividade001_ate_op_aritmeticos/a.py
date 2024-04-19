# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Leonardo Barbosa
# Data: 19/04/2024
# Faça um programa que peça 3 valores , depois calcule e imprima  a soma e a multiplicação desses valores.

#imports
import os


os.system('cls')

print('-' * 70)
print('ENTRADA DE DADOS')
print('-' * 70)

# Entrada
valor1 = float(input('Entre com o primeiro valor: '))
valor2 = float(input('Entre com o segundo valor: '))
valor3 = float(input('Entre com o terceiro valor: '))

# Processamento
soma = valor1 + valor2 + valor3
multiplicacao = valor1 * valor2 * valor3

# Saída
print('-' * 70)
print('RESULTADOS')
print('=' * 70)
print(f'A soma entre {valor1} + {valor2} + {valor3} é: {soma}')
print(f'A multiplicação de {valor1} x {valor2} x {valor3} é: {multiplicacao}')
print()
