# Crie um programa que realiza a contagem de 1 até 100, usando apenas de números ímpares, ao final do processo exiba na
# tela quantos números ímpares foram encontrados nesse intervalo, assim como a soma dos mesmos.

import os


os.system('cls')

inicio = 1
fim = 100
quantidade_impar = 0
soma = 0

print(f'Os números ímpares no intervalo de 0 a 100 é: ')
for c in range(inicio, fim):
    impar = c % 2 != 0
    if impar == True:
        quantidade_impar += 1
        soma += c
        print(c,end=' | ')
print()
print(quantidade_impar)
print(soma)
