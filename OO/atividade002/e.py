# Faça um programa que some a quantidade de números pares encontrados no intervalo entre 0 e 100.

import os


os.system('cls')


class Numeros():
    def __init__(self, inicio, fim):
        self.inicio = inicio
        self.fim = fim

    def imprimir(total):
        print(f'\nOs numeros pares entre {total}')


class Quantidade(Numeros):
    def exibir_quantidade(self):
        quantidade_par = 0
        # PARA EXIBIR ATÉ 100, PRECISO COLOCAR 101, POIS O ÚLTIMO ÍNDICE NÃO ESTÁ INCLUIDO NA CONTAGEM
        for c in range(0, 101):
            par = c % 2 == 0  # RETORNA True e False
            if par == True:
                quantidade_par += 1
        # print(quantidade_par)

        # SOBRECARREGAR O MÉTODO imprimir QUE ESTÁ DENTRO DA CLASSE Numeros
        Numeros.imprimir(f'{self.inicio} e {self.fim} é: {quantidade_par}')


os.system('cls')

quantidade_pares = Quantidade(0, 100)
quantidade_pares.exibir_quantidade()
