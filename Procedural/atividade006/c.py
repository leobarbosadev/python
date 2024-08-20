# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Leonardo Barbosa
# Data: 17/06/2024
# c)Faça um programa que procure na lista numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15] e produza: 
# • O intervalo de 1 até 9
# • O intervalo de 8 até 13
# • Os números pares
# • Os números ímpares
# • Os múltiplos de 2, 3 e 4
# • Lista reversa • O produto dos intervalos 5-6 por 11-12

import os


os.system('cls')

print('-' * 80)
print('BUSCANDO NA LISTA')
print('=' * 80)

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

intervalo_1_a_9 = lista[0:9]
intervalo_8_a_13 = lista[7:13]
pares = []
impares = []
multiplo_3 = []
multiplo_4 = []
intervalo_5_6 = lista[4:6]
intervalo_11_12 = lista[10:12]
produto_1 = 0
produto_2 = 0

# Par e ímpar e múltiplo de 2
for i in range(1, len(lista)):
    if i % 2 == 0:
        pares.append(i)
    else:
        impares.append(i)

# Múltiplo de 3
for i in range(1, len(lista)):
  if i % 3 == 0:
    multiplo_3.append(i)

#Múltiplo de 4
for i in range(1, len(lista)):
  if i % 4 == 0:
    multiplo_4.append(i)

produto_1 = intervalo_5_6[0] * intervalo_11_12[0]
produto_2 = intervalo_5_6[1] * intervalo_11_12[1]

lista.reverse()

print(f'Intervalo de 1 a 9:{intervalo_1_a_9}')
print()
print(f'Intervalo de 8 a 13:{intervalo_8_a_13}')
print()
print(f'Números pares: {pares}')
print()
print(f'Números ímares: {impares}')
print()
print(f'Múltiplos de 2: {pares}')
print()
print(f'Múltiplos de 3: {multiplo_3}')
print()
print(f'Múltiplos de 4: {multiplo_4}')
print()
print(f'Lista reversa: {lista}')
print()
print(f'Produto dos intervalos 5-6 por 11-12: {produto_1} e {produto_2}')
print()