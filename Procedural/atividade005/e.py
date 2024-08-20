# Faça um programa que some a quantidade de números pares encontrados no intervalo entre 0 e 100.

import os


os.system('cls')

quantidade_par = 0

for c in range(0, 101):  # PARA EXIBIR ATÉ 100, PRECISO COLOCAR 101, POIS O ÚLTIMO ÍNDICE NÃO ESTÁ INCLUIDO NA CONTAGEM
    par = c % 2 == 0  # RETORNA True e False
    if par == True:
        quantidade_par += 1
print(f' A quantidade de números pares entre 0 e 100 é de {quantidade_par}')
print()
