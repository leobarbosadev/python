# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Leonardo Barbosa
# Data: 03/09/2024
# Faça um programa que converta metros em centímetros e milímetros.
import os


class Calcular:
    def __init__(self, metros):
        self.metros = metros

    def centimetro_milimetro(self):
        # Usar try except para tratar erros e validar
        self.metros = float(self.metros)
        centimetros = self.metros * 100
        milimetros = self.metros * 1000
        return centimetros, milimetros


os.system('cls')
entrada = input('Entre com o número que deseja fazer a conversão: ')
calcular = Calcular(entrada)
converter_cm, converter_mm = calcular.centimetro_milimetro()
# resultado = calcular.centimetro_milimetro()
print(f'O número {entrada} convertido para centimetros é {converter_cm}cm e em milimetros é {converter_mm}mm')

