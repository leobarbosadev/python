# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Leonardo Barbosa
# Data: 17/06/2024
# g) Faça um programa que sorteia os números da Mega Sena e da Lotofácil

import os
import random


os.system('cls')

print('-' * 80)
print('SORTEIO MEGA-SENA E LOTOFÁCIL')
print('=' * 80)

mega_sena = []  # Mega-sena 60 numeros
loto_facil = []  # ltofacil 25 numeros

for i in range(1, 61):
    i = int(i)
    mega_sena.append(i)
    if i <= 25:
        loto_facil.append(i)

# Fazendo o sorteio
# VAI RETORNAR 6 NÚMEROS DA LISTA mega_sena
sorteio_mega = random.sample(mega_sena, 6)
sorteio_loto = random.sample(loto_facil, 15)

sorteio_mega.sort()
sorteio_loto.sort()

print(f'Sorteio Mega-Sena: {sorteio_mega}')
print()
print(f'Sorteio Lotofácil: {sorteio_loto}')
print()