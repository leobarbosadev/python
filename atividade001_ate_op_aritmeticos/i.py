# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Leonardo Barbosa
# Data: 19/04/2024
# Faça um programa que receba um valor em reais, depois calcule quantos dólares daria para comprar com esse valor.

# imports
import os


os.system('cls')

print('-' * 70)
print('ENTRADA DE DADOS')
print('-' * 70)

# Entrada
valor_em_reais = float(input('Entre com um valor: '))

# Processamento
# valor_dolar = 5.20
# conversao_real_dolar = valor_dolar * valor_real
# conversao_dolar_real = valor_real / valor_dolar

cotacao_dolar = 5.20
conversao_em_dolar = valor_em_reais / cotacao_dolar

# Saída
print('-' * 70)
print('CONVERSÃO DE VALORES')
print('=' * 70)
print(f'R${valor_em_reais:.2f} equivalem a ${conversao_em_dolar:.2f}')
print()
