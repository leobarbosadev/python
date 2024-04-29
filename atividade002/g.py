# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Leonardo Barbosa
# Data: 29/04/2024
# G) Você está desenvolvendo um programa para determinar se três segmentos podem formar um triângulo. 
# Para isso, o programa precisa receber as medidas dos três segmentos e compará-las entre si. 
# A resposta resultante dessa comparação deve indicar se os segmentos fornecidos podem formar um triângulo ou não.

import os


os.system('cls')

# Entrada
segmento1 = int(input('Digite um valor: '))
segmento2 = int(input('Digite um valor: '))
segmento3 = int(input('Digite um valor: '))
resposta = ''

# Condicional
if (segmento1 <= 0 or segmento2 <= 0 or segmento3 <= 0):
    resposta = f'As medidas não formam um triângulo'
elif  ((segmento1 < (segmento2 + segmento3)) and (segmento2 < (segmento1 + \
                    segmento3)) and (segmento3 < (segmento1 + segmento2))):
    resposta = f'As medidas formam um triângulo'
else:
    resposta = (f'A soma dos valores: {segmento1}, {segmento2} e {segmento3}'
                + f' pode formar um triângulo')

# Saída
print()
print(resposta)
print('-' * 80)

