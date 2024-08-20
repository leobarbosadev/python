# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Leonardo Barbosa
# Data: 13/04/2024
#Faça um programa onde o usuário tenta adivinhar o número que o computador está ‘pensando’.

import os
import random


os.system('cls')

print('COMPUTADOR ADVINHO')
print('=' * 70)
numero = int(input('Insira um número entre 1 e 10: '))

numero_randomico = random.randint(1,10)

if numero_randomico == numero:
    print(f'Você acertou!!!! O número sorteado foi: {numero_randomico}')
else:
    print(f'Você errou!!! o número correto é: {numero_randomico}, tente novamente')