# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Leonardo Barbosa
# Data: 03/06/2024
# Faça um programa que imprima os valores no intervalo definidos pelo usuário.
# Defina 3 números que deverão ser ignorados,
# ou seja, que não serão impressos na tela.
import os


class Numeros:
    def __init__(self, inicio, final):
        self.inicio = inicio
        self.fim = final

    def exibir_titulo():
        print('-' * 80)
        print('*** EXCLUIR TRÊS NÚMEROS ***')
        print('=' * 80)
        print()

    def exibir_excluidos():
        print('-' * 80)
        print('NÚMEROS PARA SEREM EXCLUÍDOS')
        print('-' * 80)


class ExcluirNumeros(Numeros):
    def excluir(self):
        for c in range(inicio, fim):
            if c == numero_1 or c == numero_2 or c == numero_3:
                continue
            print(c, end=' | ')


os.system('cls')


Numeros.exibir_titulo()
inicio = int(input('Digite o início do intervalo...: '))
fim = int(input('Digite o fim do intervalo......: ')) + 1
Numeros.exibir_excluidos()
numero_1 = int(input('Entre com o 1º número a ser excluído: '))
numero_2 = int(input('Entre com o 2º número a ser excluído: '))
numero_3 = int(input('Entre com o 3º número a ser excluído: '))
excluir = ExcluirNumeros(inicio, fim)
excluir.excluir()
print()


print('-' * 80)
print()
