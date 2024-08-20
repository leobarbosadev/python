#Faça um programa que receba Se a divisão não for inteira, 2 valores, faça a divisão entre eles. 
# o programa deverá arredondar o resultado para cima e para baixo. Faça a validação para divisão por 0.

import os
import math


os.system('cls')

numero1 = float(input('Entre com um número: '))
numero2 = float(input('Entre com outro número: '))

if numero2 == 0:
    print('Não pode ser divido por 0')
# elif numero1 % numero2 == 0:
else:
    resultado = numero1 / numero2
    arredondar_para_cima = math.ceil(resultado)
    arredondar_para_baixo = math.floor(resultado)

print(f'O resultado de {numero1} por {numero2} é {resultado} '
      +f'arredondado para cima é {arredondar_para_cima} '
      +f'arredondado para baixo é {arredondar_para_baixo}')