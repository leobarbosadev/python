import math
import os


os.system('cls')

print('-' * 50)
print('ESTUDO DA BIBLIOTECA MATEMÁTICA MATH')
print('=' * 50)
print()

#Entrada de dados
numero_decimal = float(input('Entre com um número decimal: '))

#Processamento
arrendondar_para_cima = math.ceil(numero_decimal)
arrendondar_para_baixo = math.floor(numero_decimal)

#Saída
print('-' * 50)
print(f'O número {numero_decimal} arredondado para cima é: {arrendondar_para_cima}')
print(f'O numero {numero_decimal} arrendondado para baixo é: {arrendondar_para_baixo}')
print('-' * 50)