# Faça um programa que imprima os números primos entre 0 e 100.
import os


class Numeros:
    def __init__(self, inicio, fim):
        self.inicio = inicio
        self.fim = fim

    # def imprime(quantidade):
    #     print(f'\nOs numeros primos entre: {quantidade}')


class Primos(Numeros):
    def mostra_primos(self):
        for c in range(0, 101):
            contador = 0  # QUANTAS VEZES O NÚMERO C É DIVIDIDO
            for c2 in range(1, 100):
                if c % c2 == 0:
                    contador += 1
            if contador == 2:
                print(f'{c}', end=' | ')
        # Numeros.imprime(f'{self.inicio} e {self.fim} é: {c}')


os.system('cls')

exibir_primos = Primos(0, 100)
exibir_primos.mostra_primos()
