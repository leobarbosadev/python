# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Leonardo Barbosa
# Data: 17/06/2024
# e) Crie uma lista com 6 nomes, depois verifique se o nome ‘Pedro’ está nessa lista.

import os


os.system('cls')

os.system('cls')

print('-' * 80)
print('PEDRO TÁ LISTA?')
print('=' * 80)

nomes = []

while len(nomes)  <= 5: # PARA CRIAR UMA LISTA COM 6 NOMES, DEFINO O TAMANHO COMO 5 (DE 0 A 5)
  entrada = input('Digite um nome: ').capitalize()
  nomes.append(entrada)
print()
  # print(nomes) SE EU DEIXAR ELE ONDE TÁ, ELE VAI INCREMENTANDO A LISTA E MOSTRANDO
print(nomes)
if 'Pedro' in nomes:
  print('Pedro encontrado')
  print()
else:
  print('Na lista digitada não foi encotrado Pedro')
  print()