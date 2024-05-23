# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Leonardo Barbosa
# Data: 23/05/2024
#Faça um programa que receba um número inteiro e mostre na tela:
#A quantidade de unidades, a quantidade de dezenas, a quantidade de centenas e a quantidade de milhares.

import os


os.system('cls')

numero = int(input('Entre com um número inteiro: '))

unidade = (numero % 10)
dezena = (numero - unidade)
centena = (numero // 100)
milhar = (numero // 1000)


print(f'{unidade} unidades')
# print(f'{dezena} dezenas')
# print(f'{centena} centenas')
# print(f'{milhar} unidade de milhar')