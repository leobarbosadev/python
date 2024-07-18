# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Leonardo Barbosa
# Data:
#Crie uma função que receba a altura e o peso de uma pessoa.
# Depois retorne o seu IMC.
import os


os.system('cls')

def calcular_imc():
    calculo_imc = peso / (altura * altura) # altura **2
    
    return calculo_imc
    
    
altura = float(input('Entre com sua altura (em m): '))
peso = float(input('Entre com o seu peso (em kg): '))

imc = calcular_imc()

print(f'O seu imc é de {imc:.2f}')
print()