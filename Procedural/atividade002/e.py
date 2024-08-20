# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Leonardo Barbosa
# Data: 26/04/2024
# E) A empresa "TravelCalc" está desenvolvendo um sistema de cálculo de preços de passagens de ônibus com base na distância da viagem. 
# Eles precisam de um programa que solicite ao usuário a distância a desejada e, em seguida, 
# calcule o preço da passagem de acordo com as políticas da empresa. 
# Segundo essas políticas, viagens de até 200 km têm um custo de R$0,70 por km rodado, 
# enquanto viagens acima dessa distância passam a custar R$0,40 por km rodado.

import os


os.system('cls')

print('-' * 80)
print('Valor da passagem')
print('-' * 80)

distancia = float(input('Entre com a distância: '))
resposta = ''

if distancia <= 200:
    valor_passagem = distancia * 0.70
    resposta = (f'A distância da viagem é de {distancia} km, '
    + f'o valor da passagem é de R${valor_passagem:.2f}')
else:
    valor_passagem = distancia * 0.40
    resposta = (f'A distância da viagem é de {distancia} km, '
    + f'o valor da passagem é de R${valor_passagem:.2f}')
    
print('-' * 80)
print(resposta)
print()
