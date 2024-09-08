# Crie um programa que realiza a contagem de 1 até 100, usando apenas de números ímpares, ao final do processo exiba na
# tela quantos números ímpares foram encontrados nesse intervalo, assim como a soma dos mesmos.

import os


class Numeros:
    def __init__(self, inicio=1, fim=100):
        self.inicio = inicio
        self.fim = fim

    def exibir_quantidade(valores):
        print(f'\nA quantidade de números impares de  a 100 é: {valores}')

    def exibir_soma(soma):
        print(f'A soma dos números impares de  a 100 é: {soma}')

class MostrarImpar(Numeros):
    def exibir_impares(self):
        quantidade_impar = 0
        c = 0
        soma = 0
        for c in range(self.inicio, self.fim):
            impar = c % 2 != 0
            if impar == True:
                quantidade_impar += 1
                soma += c
                print(c, end=' | ')

        Numeros.exibir_quantidade(quantidade_impar)
        Numeros.exibir_soma(soma)


os.system('cls')
mostrar = MostrarImpar(1, 100)
mostrar.exibir_impares()
print()