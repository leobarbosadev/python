# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Leonardo Barbosa
# Data: 03/09/2024
# Faça um programa que receba um valor em reais, depois calcule quantos dólares daria para comprar com esse valor.
import os


valor_dolar= 5.65
class Moeda:
    def __init__(self, valor):
        self.valor = valor
        

    def converter_moeda(self):
        self.valor = float(self.valor)
        converter_real_dolar = valor_dolar * self.valor
        return converter_real_dolar
    
os.system('cls')
entrada = float(input('Entre com um valor em R$: '))
converter = Moeda(entrada)
resultado = converter.converter_moeda()
print(f'R${entrada:.2f} = US${resultado}')

    
    