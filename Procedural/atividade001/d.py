# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Leonardo Barbosa
# Data: 19/04/2024
# Faça um programa que receba e divida 2 números. A saída da divisão precisará ser formatada com 4 casas decimais.

#import
import os


os.system('cls')

print('-' * 70)
print('ENTRADA DE DADOS')
print('-' * 70)

# Entrada
valor1 = float(input('Entre com o primeiro número: '))
valor2 = float(input('Entre com o segundo núemro.: '))

#Porcessamento
divisao = valor1 / valor2
# PRECISO TRATAR DIVISÃO POR 0 (try/catch)
#Saída
print('-' * 70)
print('RESULTADO')
print('=' * 70)
print(f'O resultado da divisão é: {divisao:.4f}')
print('-' * 70)
print()
