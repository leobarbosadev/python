# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Leonardo Barbosa
# Data:
# Faça um programa que peça o ano do seu nascimento e calcule a sua idade.

#imports
import os
import datetime


os.system('cls')

print('-' * 70)
print('ENTRADA DE DADOS')
print('-' * 70)

# Entrada
ano_nascimento = int(input('Digite o ano do seu nascimento: '))

# Processamento
ano_atual = datetime.datetime.now().year
idade = int(ano_atual) - ano_nascimento

# Saída
print('-' * 70)
print('RESULTADO')
print()
print(f'Sua idade é: {idade}')
print()