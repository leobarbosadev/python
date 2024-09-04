# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Leonardo Barbosa
# Data: 03/09/2024
# Faça um programa que receba e divida 2 números. A saída da divisão precisará ser formatada com 4 casas decimais.
import os


class Calcular:
    def __init__(self, valor1, valor2):
        self.valor1 = valor1
        self.valor2 = valor2
        
    def divisao(self, valor1, valor2):
        # Usar try except para tratar erros e validar
        resultado = float(valor1) / float(valor2)
        return resultado
    
os.system('cls')
valor1 = input('Entre com o primeiro valor: ')
valor2 = input('Entre com o segundo valor.: ')
calcular = Calcular(valor1,valor2)
resultado = calcular.divisao(valor1, valor2)
print(f'A divisão de {valor1} por {valor2} é: {resultado:.4f}')
