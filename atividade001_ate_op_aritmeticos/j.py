# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Leonardo Barbosa
# Data: 19/04/2024
# Faça um programa com entrada de dados para calcular o perímetro de um retângulo.

# imports
import os


os.system('cls')

print('-' * 70)
print('ENTRADA DE DADOS')
print('-' * 70)

# Entrada
base = float(input('Entre com o valor da base do retângulo: '))
altura = float(input('Entre com o valor da altura do retângulo: '))

# Processamento
perimetro = 2 * (base + altura)

# Saída
print('-' * 70)
print('PERÍMETRO DO RETÂNGULO')
print('=' * 70)
print(f'O perímetro do retângulo de base {base:.2f} e altura {altura:.2f} é de {perimetro:.2f}')
