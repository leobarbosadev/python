# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Leonardo Barbosa
# Data: 26/04/2024
# D) A empresa "SalaryBoost" está implementando um sistema automatizado para calcular os aumentos salariais de seus funcionários com base 
# em critérios específicos. Eles precisam de um programa que receba como entrada o salário atual de um funcionário e, em seguida, 
# calcule o novo salário com base em determinadas condições. 
# Essas condições incluem um aumento de 5% caso o salário atual seja superior a R$1500,00, 
# e um aumento de 10% caso o salário atual seja inferior a R$1000,00. Além disso, 
# o programa deve garantir que o salário informado não seja igual a zero ou negativo, pois isso não seria válido.

import os


os.system('cls')

print('-' * 80)
print('Calculando salários')
print('-' * 80)

salario = float(input('Entre com o seu salário R$: '))
resposta = ''

if salario <= 0:
    resposta =f'Salário inválido, digite um valor maior que 0'
elif salario >= 1500:
    novo_salario = salario + (salario * 0.05)
    resposta = f'Seu salário é de R${salario:.2f}, seu novo salário será de R${novo_salario:.2f}'
elif salario <= 1000:
    novo_salario = salario + (salario * 0.1)
    resposta = f'Seu salário é de R${salario:.2f}, seu novo salário será de R${novo_salario:.2f}'
else:
    resposta = f'Seu salário não sofrerá alteração'
    
print('-' * 80)
print(resposta)
print()