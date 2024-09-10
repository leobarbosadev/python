# Faça um programa que imprima os números primos entre 0 e 100.
import os

                
class Numeros: # superclasse ou classe pai
    def __init__(self, inicio, fim):
        self.inicio = inicio
        self.fim = fim
        
    def mostrar_primos(self,inicio, fim):
        print('Não vai imprimir nada') # Vai ser sobrecarregado, para mostrar na tela, tenho que usar o super

class Primos(Numeros): # subclasse ou classe classe derivada
    def __init__(self, inicio, fim):
        self.inicio = inicio
        self.fim = fim
        
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
print('NUMEROS PRIMOS ENTRE 0 E 100')
exibir_primos = Primos(0, 100)
exibir_primos.mostra_primos()

############# JEITO QUE EU TINHA FEITO #############
# class Numeros:
#     def __init__(self, inicio, fim):
#         self.inicio = inicio
#         self.fim = fim


# class Primos(Numeros):
#     def mostra_primos(self):
#         for c in range(0, 101):
#             contador = 0  # QUANTAS VEZES O NÚMERO C É DIVIDIDO
#             for c2 in range(1, 100):
#                 if c % c2 == 0:
#                     contador += 1
#             if contador == 2:
#                 print(f'{c}', end=' | ')