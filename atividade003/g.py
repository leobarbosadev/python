# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Leonardo Barbosa
# Data: 13/04/2024
# Faça um programa que peça os valores de a, b e c de uma equação do 2º grau.
# Calcule as raízes da equação do 2º grau seguindo a fórmula: Δ = b² - 4ac, x = (-b ± raiz(Δ)) / (2a).

import os
import math


os.system('cls')

a = float(input('Entre com um valor: '))
b = float(input('Entre com um valor: '))
c = float(input('Entre com um valor: '))
print()
delta = math.pow(b, 2) - 4 * a * c

if delta <= 0:
    print('Não possui Delta menor ou igual a 0')
else:
    raiz_delta = math.sqrt(delta)
    x1 = (-b + raiz_delta) / (2 * a)
    x2 = (-b - raiz_delta) / (2 * a)
    print(f'O resultado de x1 é: {x1} e o resultado de x2 é: {x2}')
    
print('-' * 70)
print()
