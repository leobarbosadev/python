# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Leonardo Barbosa
# Data: 03/09/2024
# Faça um programa que receba um número inteiro e mostre o sucessor e antecessor.
import os


class Antes_e_depois:
    def __init__(self, valor):
        self.valor = valor

    def antecesor_sucessor(self):
        # Usar try except para tratar erros e validar
        self.valor = int(self.valor)
        antecesor = self.valor - 1
        sucessor = self.valor + 1
        return antecesor, sucessor


os.system('cls')
valor = input('Entre com o valor par vermos seu antecessor e sucessor: ')
adjacentes = Antes_e_depois(valor)
antecessor, sucessor = adjacentes.antecesor_sucessor()
# POSSO PASSA ISSO DENTRO DO return DO MÉTODO def antecessor_sucessor
print(f'O antecessor de {valor} é {antecessor} e o sucessor é {sucessor}')
print()
