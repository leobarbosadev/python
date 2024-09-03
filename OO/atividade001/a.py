# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Leonardo Barbosa
# Data: 02/09/2024
# Faça um programa que peça 3 valores , depois calcule e imprima  a soma e a multiplicação desses valores.
import os



# def validar(self, valor1, valor2, valor3):
#         if valor1.isalpha() or valor2.isalpha() or valor3.isalpha():
#             print('Teste')

class Calcular:
    def __init__(self, valor1, valor2, valor3):
        self.valor1 = valor1
        self.valor2 = valor2
        self.valor3 = valor3

    def somar(self, valor1, valor2, valor3):
        soma = valor1 + valor2 + valor3
        return soma

    def multiplicar(self, valor1, valor2, valor3):
        multiplicar = valor1 * valor2 * valor3
        return multiplicar


while True:
    opcao = input('1 - Somar\n2 - Multiplicar\n0 - Sair\n')

    if opcao == '1':
        print('SOMA')
        valor1 = input('Entre com o primeiro valor: ')
        valor2 = input('Entre com o segundo valor.: ')
        valor3 = input('Entre com o terceiro valor: ')
        soma = Calcular(valor1, valor2, valor3)
        somando = soma.somar(valor1, valor2, valor3)
        input(f'O Resultado da soma é: {somando}')
        os.system('cls')

    if opcao == '2':
        print('MULTIPLICACAO')
        valor1 = float(input('Entre com o primeiro valor: '))
        valor2 = float(input('Entre com o segundo valor.: '))
        valor3 = float(input('Entre com o terceiro valor: '))
        multiplica = Calcular(valor1, valor2, valor3)
        multiplicando = multiplica.multiplicar(valor1, valor2, valor3)
        input(f'O resultado da multiplicacao é: {multiplicando}')
        os.system('cls')