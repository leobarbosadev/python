# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Leonardo Barbosa
# Data: 13/04/2024
#Faça um programa que receba um ângulo qualquer. Em seguida, calcule o seno, cosseno e tangente do ângulo, limitando a saída a 2 casas decimais.

import os
import math


angulo = float(input('Entre com um valor para um ângulo: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print(f'O ângulo digitado foi {angulo}°, seu seno é: {seno:.2f} '
      +f'seu cosseno é: {cosseno:.2f} e sua tangente é: {tangente:.2f}')