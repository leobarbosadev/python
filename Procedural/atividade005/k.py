# Crie um programa que pede que o usuário digite um nome ou uma frase, 
# verifique se esse conteúdo digitado é um palíndromo ou não, exibindo em tela esse resultado.

import os


os.system('cls')

print('É PALÍNDROMO OU NÃO?')

frase = input('Entre com o nome ou frase: ').lower()
palindromo = frase[::-1]

if frase == palindromo:
    print(f'A palavra ou frase {frase}, é palíndromo')
else:
    print(f'A palavra ou frase {frase}, não é palíndromo')
