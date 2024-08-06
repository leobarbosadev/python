# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Leonardo Barbosa
# Data:
# Crie uma função que receba uma lista de números.
# Depois retorne duas listas com os números pares, os números ímpares,
# a quantidade de números pares e a quantidade de números ímpares.

#-----------------------USAR LIST COMPREHENSION-----------------------
import os
import random


os.system('cls')

lista_numeros = [] # TENTAR USAR O RANDINT
lista_par = []
lista_impar = []

for i in range (3):
    entrada = int(input(f'Entre com o {i+1}º número: '))
    lista_numeros.append(entrada)
print()

# lista_numeros = random.randint

def listar(lista_numeros):

    for i in lista_numeros:
        lista_par.append(i) if i % 2 == 0 else lista_impar.append(i)
        # if i % 2 == 0:
        #     lista_par.append(i)
        # else:
        #     lista_impar.append(i)

    quantidade_par = len(lista_par)
    quantidade_impar = len(lista_impar)
    return lista_par, lista_impar, quantidade_par,quantidade_impar

par, impar, quantidade_par, quantidade_impar = listar(lista_numeros)

print(f'A lista de par é : {lista_par} e a quantidade de números pares é {quantidade_par}')
print(f'A lista de ímpar é : {lista_impar} e a quantidade de números ímpares é {quantidade_impar}')
print()




