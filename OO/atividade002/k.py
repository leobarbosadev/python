# Crie um programa que pede que o usuário digite um nome ou uma frase, 
# verifique se esse conteúdo digitado é um palíndromo ou não, exibindo em tela esse resultado.
import os

class Frase:
    def __init__(self, frase):
        self.frase = frase

class VerificarPalindromo(Frase):
    def verificar(self):
        palindromo = frase[::-1]

        if self.frase == palindromo:
            print(f'A palavra ou frase {self.frase}, é palíndromo')
        else:
            print(f'A palavra ou frase {self.frase}, não é palíndromo')


os.system('cls')

print('É PALÍNDROMO OU NÃO?')
frase = input('Entre com o nome ou frase: ').lower()
mostar = VerificarPalindromo(frase)
palindromo = mostar.verificar()

