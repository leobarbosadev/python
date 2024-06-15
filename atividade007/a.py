# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Leonardo Barbosa
# Data: 17/06/2024
# Faça um programa que leia um número indeterminado de notas (pressione ‘s’ ou ‘0’ para sair).

import os


os.system('cls')

while True:
  notas = []
  print('Digite "0" ou "s" para sair do sistema')
  entrada = input('Entre com uma nota: ')
  notas.append(entrada)
  print()
  
  if entrada == '0' or entrada == 's'.lower():
    print('Sistema finalizado')
    print()
    break
  else:
    notas.append(entrada)

  # if not (entrada == '0' or entrada.lower() == 's'):
  #   notas.append(entrada)
  # else:
  #   sair = input('0 ou s achado, sair? ').lower()
  #   if sair == '0' or sair == 's':
  #     print('Programa finalizado!!!')
  #     break