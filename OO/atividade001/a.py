# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Leonardo Barbosa
# Data: 02/09/2024
# Faça um programa que peça 3 valores , depois calcule e imprima  a soma e a multiplicação desses valores.
import os


class Calcular:
    def __init__(self, valor1, valor2, valor3):
        self.valor1 = valor1
        self.valor2 = valor2
        self.valor3 = valor3

    def somar(self):
        # SEM try except
        # self.valor1 = float(self.valor1)
        # self.valor2 = float(self.valor2)
        # self.valor3 = float(self.valor3)
        # soma = self.valor1 + self.valor2 + self.valor3
        # return soma

        # COM try except
        try:
            soma = float(self.valor1) + float(self.valor2) + float(self.valor3)
            return soma
        except (TypeError, ValueError):
            return ('Digite somente numeros!!')

    def multiplicar(self):
        # SEM try except
        # self.valor1 = float(self.valor1)
        # self.valor2 = float(self.valor2)
        # self.valor3 = float(self.valor3)
        # multiplicar = self.valor1 * self.valor2 * self.valor3
        # return multiplicar

        # COM try except
        try:
            multiplicar = float(self.valor1) * \
                float(self.valor2) * float(self.valor3)
            return f'O resultado da multiplicacao é: {multiplicar}'
        except (TypeError, ValueError):
            return ('Digite somente numeros!!')


while True:
    opcao = input('1 - Somar\n2 - Multiplicar\n0 - Sair\n')

    if opcao == '1':
        print()
        print('SOMA')
        valor1 = input('Entre com o primeiro valor: ')
        valor2 = input('Entre com o segundo valor.: ')
        valor3 = input('Entre com o terceiro valor: ')
        soma = Calcular(valor1, valor2, valor3)
        somando = soma.somar()
        input(f'O Resultado da soma é: {somando}')
        os.system('cls')

    if opcao == '2':
        print()
        print('MULTIPLICACAO')
        valor2 = input('Entre com o segundo valor.: ')
        valor3 = input('Entre com o terceiro valor: ')
        valor1 = input('Entre com o primeiro valor: ')
        multiplica = Calcular(valor1, valor2, valor3)
        multiplicando = multiplica.multiplicar()
        # input(f'O resultad:o da multiplicacao é: {multiplicando}')
        input(multiplicando)
        os.system('cls')

    if opcao == '0':
        print()
        print('Programa finalizado!!')
        break
