# Faça um programa que some a quantidade de números pares encontrados no intervalo entre 0 e 100.

import os


class Numeros(): # superclasse ou classe pai
    def __init__(self, inicio, fim):
        self.inicio = inicio
        self.fim = fim

    def imprimir(self, inicio, fim):
        print('Não vai imprimir nada') # Vai ser sobrecarregado, para mostrar na tela, tenho que usar o super


class Quantidade(Numeros): # subclasse ou classe classe derivada
    def __init__(self, inicio, fim):
        self.inicio = inicio
        self.fim = fim

    def exibir_quantidade(self):
        quantidade_par = 0
        # PARA EXIBIR ATÉ 100, PRECISO COLOCAR 101, POIS O ÚLTIMO ÍNDICE NÃO ESTÁ INCLUIDO NA CONTAGEM
        for c in range(0, 101):
            par = c % 2 == 0  # RETORNA True e False
            if par == True:
                quantidade_par += 1
        # print(quantidade_par)

        print(
            f'a quantidade de numeros pares entre 0 e 100 é: {quantidade_par}')


os.system('cls')

quantidade_pares = Quantidade(0, 100)
quantidade_pares.exibir_quantidade()

############# JEITO QUE EU TINHA FEITO #############
# class Numeros():
#     def __init__(self, inicio, fim):
#         self.inicio = inicio
#         self.fim = fim

#     def imprimir():
#         print(f' A quantidade de números pares entre 0 e 100 é de')

# class Quantidade(Numeros):
#     quantidade_par = 0
#     def exibir_quantidade():
#         for c in range(0, 101):  # PARA EXIBIR ATÉ 100, PRECISO COLOCAR 101, POIS O ÚLTIMO ÍNDICE NÃO ESTÁ INCLUIDO NA CONTAGEM
#             par = c % 2 == 0  # RETORNA True e False
#         if par == True:
#             quantidade_par += 1