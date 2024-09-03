# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Leonardo Barbosa
# Data: 03/09/2024
# Faça um programa que peça 4 notas, após a entrada de dados calcular a média das notas digitadas.
import os


class Notas:
    def __init__(self, nota1, nota2, nota3, nota4):
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3
        self.nota4 = nota4
        
    def calcular_media(self, nota1, nota2, nota3, nota4):
        # Usar try except para tratar erros e validar
        soma = float(nota1) + float(nota2) + float(nota3) + float(nota4)
        media = soma / 4
        return media


os.system('cls')
nota1 = input('Entre com a primeira nota: ')
nota2 = input('Entre com a segunda nota.: ')
nota3 = input('Entre com a terceira nota: ')
nota4 = input('Entre com a quarta nota..: ')
notas = Notas(nota1, nota2, nota3, nota4)
resultado = notas.calcular_media(nota1, nota2, nota3, nota4)
print(f'A média das notas {nota1}, {nota2}, {nota3}, {nota4} é: {resultado}')
    