# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Leonardo Barbosa
# Data: 29/04/2024
#H) A empresa "RootCalc" está desenvolvendo um software de cálculo de raízes de equações quadráticas para auxiliar engenheiros e cientistas em suas análises e projetos. Eles precisam de um programa que calcule as raízes da equação quadrática 𝑥²−6𝑥+5 sem depender de funções ou métodos predefinidos, utilizando apenas os conceitos e operações básicas aprendidos até o momento. Essas raízes são conhecidas como 𝑥’ = 5 e 𝑥’’ = 1, e o programa deve ser capaz de calcular essas raízes de forma precisa, seguindo os princípios matemáticos fundamentais.

import os
a = 1
b = -6
c = 5
resposta = ''

# Processamento
delta = b**2 - 4*a*c
raiz_de_delta = delta**(1/2)

# Condicionais
if delta < 0:
    resposta = f'Não tem uma raiz'
else:
    x1 = (-b + raiz_de_delta)/(2*a)
    x2 = (-b - raiz_de_delta)/(2*a)
    resposta = f'Os valores das raízes são: {x1:.2f} e {x2:.2f}'

# Saída
print()
print(resposta)
print('-' * 70)
