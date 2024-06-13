# a)Crie a lista [1, 2, 3, 5, 6] e depois insira o valor que está faltando na posição correta.

import os


os.system('cls')

print('-' * 70)
print('INSERINDO VALOR NA POSIÇÃO CERTA')
print('=' * 70)

lista = [1, 2, 3, 5, 6]
print(f'Lista original: {lista}')

# Inserindo o número 4 no índice 3
inserir_item_lista = lista.insert(3, 4)

print(f'Lista completa: {lista}')

#Colocar input e sort()