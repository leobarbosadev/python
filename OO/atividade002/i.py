# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Leonardo Barbosa
# Data: 03/06/2024
# Faça um algoritmo que imprima a frase "estou em looping" e, em seguida,
# solicite ao usuário digitar uma letra.
# Caso a letra seja o “f" finalize a aplicação.
# Do contrário, imprima novamente a mesma frase até que o caractere “f" seja digitado.

import os


class Letras:
    def __init__(self, letra):
        self.letra = letra


class VerificarLetra(Letras):
    def verificar(self):
        if self.letra != 'f'.lower():
            self.letra = (
                'Estou em Looping... digite uma letra [f - Finalizar]: ')
        else:
            print('Aplicação finalizada\n')


os.system('cls')

print('-' * 80)
print('*** ESTOU EM LOOPING ***')
print('=' * 80)

while (True):
    letra = input(
        'Estou em Looping... digite uma letra [f - Finalizar]: ').lower()
    if letra != 'f'.lower():
        letras = VerificarLetra(letra)
        letras.verificar()
    else:
        print('Aplicação finalizada\n')
        break
print('-' * 80)
print()
