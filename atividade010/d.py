# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Leonardo Barbosa
# Data:
# Crie uma função que receba uma temperatura
# em fahrenheit e retorne o valor em graus célsius
import os


os.system('cls')


def converter_graus():
    temperatura_convertida = (temperatura - 32) * 5/9

    return temperatura_convertida


temperatura = float(input('Entre com a temperatura em Fahrenheit: '))

convertendo = converter_graus()

print(f'A temperatura {temperatura} °F é igual a {convertendo:.2f} °C')
print()
