# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Leonardo Barbosa
# Data: 03/06/2024
#Faça um programa que calcule os números primos 
# em um intervalo pré-determinado pelo usuário.

# entre 0 e 20 = 2, 3, 5, 7, 11, 13, 17 e 19

import os


os.system('cls')

inicio = int(input('Entre com o início do intervalo: '))
fim = int(input('Entre com o final do intervalo....:'))

for c in range(inicio, fim):
    