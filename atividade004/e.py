#Faça um programa que receba uma frase e, 
# em seguida, mostre quantas vezes as vogais foram utilizadas.

import os


os.system('cls')

frase = input('Digite uma frase: ').upper()

letra_a = frase.count('A')
letra_e = frase.count('E')
letra_i = frase.count('I')
letra_o = frase.count('O')
letra_u = frase.count('U')

print(f'A vogal A foi usada {letra_a} vezes\n'
      + f'A vogal E foi usada {letra_a} vezes\n'
      + f'A vogal I foi usada {letra_a} vezes\n'
      + f'A vogal O foi usada {letra_a} vezes\n'
      + f'A vogal U foi usada {letra_a} vezes\n')
