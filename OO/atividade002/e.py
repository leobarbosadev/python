# Faça um programa que some a quantidade de números pares encontrados no intervalo entre 0 e 100.

import os


os.system('cls')

class Numeros():
    def __init__(self, inicio, fim):
        self.inicio = inicio
        self.fim = fim
        
    def imprimir():
        print(f' A quantidade de números pares entre 0 e 100 é de')

class Quantidade(Numeros):
    quantidade_par = 0
    def exibir_quantidade():
        for c in range(0, 101):  # PARA EXIBIR ATÉ 100, PRECISO COLOCAR 101, POIS O ÚLTIMO ÍNDICE NÃO ESTÁ INCLUIDO NA CONTAGEM
            par = c % 2 == 0  # RETORNA True e False
        if par == True:
            quantidade_par += 1
            

