# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Leonardo Barbosa
# Data: 26/04/2025
# C) A empresa "SafeDrive" está desenvolvendo um sistema de monitoramento de velocidade para ajudar a promover a segurança nas estradas. 
# Eles precisam de um programa que permita aos usuários inserir a velocidade de um carro e, 
# em seguida, exibir na tela uma mensagem adequada com base na velocidade fornecida. 
# O objetivo principal é alertar os motoristas caso ultrapassem o limite de velocidade de 60 km/h, 
# incentivando-os a dirigir dentro dos limites legais e, assim, reduzir o risco de acidentes.

import os


os.system('cls')

print('-' * 80)
print('Velocidade do carro')
print('-' * 80)

velocidade = float(input('Entre com a velocidade: '))
resposta = ''

if velocidade > 60.0:
    resposta = f'Você está dirigindo na velocidade de {velocidade} km/h, está acima do limite permitido da via de 60 km/h'
    
else:
    resposta = f'Você está dirigindo na velocidade de {velocidade} km/h, e está dentro do limite de velocidade'

print('-' * 80)
print(resposta)
print()
    