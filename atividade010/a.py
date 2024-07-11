# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Leonardo Barbosa
# Data:
# Crie uma função que receba uma lista de números.
# Depois retorne duas listas com os números pares, os números ímpares,
# a quantidade de números pares e a quantidade de números ímpares.

#USAR LIST COMPREHENSION-----------------------
import os


os.system('cls')

lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista_par = []
lista_impar = []

def listar(*lista_numeros):
    quantidade_par = 0
    quantidade_impar = 0
    for i in lista_numeros:
        i = int(i)
        if i % 2 == 0:
            lista_par.append(i)
            
        else:
            lista_impar.append(i)
            
    return quantidade_par, quantidade_impar

quantidade_par, quantidade_impar = listar(*lista_numeros)

print(f'A lista de par é : {lista_par} e a quantidade de números pares é {len(lista_par)}')
print(f'A lista de ímpar é : {lista_impar} e a quantidade de números ímpares é {len(lista_impar)}')
print()

