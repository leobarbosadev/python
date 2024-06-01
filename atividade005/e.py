 # Faça um programa que some a quantidade de números pares encontrados no intervalo entre 0 e 100.

import os


os.system('cls')

quantidade_par = 0

for c in range(0, 101):  # PARA EXIBIR ATÉ 100, PRECISO COLOCAR 101, POIS O ÚLTIMO ÍNDICE NÃO ESTÁ INCLUIDO NA CONTAGEM
    # numero = int(c + 1)
    par = c % 2 == 0  # RETORNA True e False
    # print(numero)
    # print(par)
    if par == True: # POSSO JOGAR O QUE ESTÁ NA LINHA 12 DIRETO AQUI DENTRO
        quantidade_par += 1
    # print(c , end=' | ')

print(quantidade_par)
