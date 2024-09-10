# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Leonardo Barbosa
# Data: 03/06/2024
# Faça um algoritmo que imprima a frase "estou em looping" e, em seguida,
# solicite ao usuário digitar uma letra.
# Caso a letra seja o “f" finalize a aplicação.
# Do contrário, imprima novamente a mesma frase até que o caractere “f" seja digitado.

import os


class Letras: # superclasse ou classe pai
    def __init__(self, letra):
        self.letra = letra

    def verificar(self, letra):
        print('Não vai imprimir nada') # Vai ser sobrecarregado, para mostrar na tela, tenho que usar o super


class VerificarLetra(Letras): # subclasse ou classe classe derivada
    def __init__(self, letra):
        self.letra = letra

    def verificar(self):
        while True:
            self.letra = input('Estou em Looping... digite uma letra [f - Finalizar]: ').lower()
            if self.letra == 'f'.lower():
                print('Aplicação finalizada\n')
                break


os.system('cls')

print('-' * 80)
print('*** ESTOU EM LOOPING ***')
print('=' * 80)
letra = input('Estou em Looping... digite uma letra [f - Finalizar]: ').lower()
letras = VerificarLetra(letra)
letras.verificar()
print('-' * 80)
print()
