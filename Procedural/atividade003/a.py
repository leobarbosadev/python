# Faça um programa que receba um valor e mostre sua raiz quadrada. Para raízes que não são exatas, arredonde para cima ou para baixo.
# Faça a validação para números negativos, avisando ao usuário que o resultado será um número complexo.

import os
import math


os.system('cls')

# Entrada
numero = int(input('Entre com um número inteiro: '))

# Condicional
if numero < 0:
    print('Número negativo, o resultado será um número complexo')
else:
    raiz = math.sqrt(numero)
    raiz_arredondada = math.floor(raiz)

print(f'A raiz de {numero} é {raiz}, sua raiz arredondada é {raiz_arredondada}')