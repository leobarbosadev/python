# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Leonardo Barbosa
# Data: 17/06/2024
# a)Faça um programa que leia um número indeterminado de notas (pressione ‘s’ ou ‘0’ para sair).

import os


os.system('cls')

print('-' * 80)
print('NOTAS')
print('=' * 80)


notas = []
entrada = ""

while True:
  entrada = input('Digite uma nota: [0 ou s - Sair] ')
  notas.append(entrada)

  if entrada.lower() == 's' or entrada == '0':
    print()
    print('Programa finalizado!!!')
    print()
    notas.pop()
    break

    # if not (entrada == '0' or entrada.lower() == 's'):
    #   notas.append(entrada)
    # else:
    #   sair = input('0 ou s achado, sair? ').lower()
    #   if sair == '0' or sair == 's':
    #     print('Programa finalizado!!!')
    #     break
