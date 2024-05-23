#Faça um programa que leia uma frase e depois exiba na tela:
#A frase em minúsculas, a frase em maiúsculas, a quantidade de caracteres na frase e quantas letras tem a 2ª palavra na frase.

import os


os.system('cls')

frase = input('Entre com uma frase: ')

maiusculas = frase.upper()
minusculas = frase.lower()
quantidade = len(frase)
lista = frase.split(' ')
palavra = ''.join(lista[1])
segunda_palavra = len(palavra)

print(f'A frase digitada foi: {frase}\n'
      + f'Tudo em maiúsculo: {maiusculas}\n'
      + f'Tudo em minúsculo: {minusculas}\n'
      + f'A frase tem {quantidade} caracteres\n'
      + f'A segunda palavra tem {segunda_palavra} caracteres')