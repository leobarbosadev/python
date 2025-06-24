# Crie um programa que pede que o usuário digite um nome ou uma frase,
# verifique se esse conteúdo digitado é um palíndromo ou não, exibindo em tela esse resultado.
import os


class Frase:  # superclasse ou classe pai
    def __init__(self, frase, frase2):
        self.frase = frase
        self.frase2 = frase2

    def verificar(self, frase, frase2):
        print('Não vai imprimir nada') # Vai ser sobrecarregado, para mostrar na tela, tenho que usar o super


class VerificarPalindromo(Frase):  # subclasse ou classe classe derivada
    def __init__(self, frase, frase2):
        self.frase = frase
        self.frase2 = frase2

    def verificar(self):
        palindromo = self.frase2[::-1]

        if self.frase2 == palindromo:
            print(f'A palavra ou frase "{frase}" é palíndromo')

        else:
            print(f'A palavra ou frase "{frase}" não é palíndromo')


os.system('cls')

print('É PALÍNDROMO OU NÃO?')
frase = input('Entre com o nome ou frase: ').strip().lower()
frase2 = frase.replace(' ', '')
print()
mostar = VerificarPalindromo(frase, frase2)
palindromo = mostar.verificar()

############# JEITO QUE EU TINHA FEITO #############
# class Frase:
#     def __init__(self, frase):
#         self.frase = frase

# class VerificarPalindromo(Frase):
#     def verificar(self):
#         palindromo = frase[::-1]

#         if self.frase == palindromo:
#             print(f'A palavra ou frase {self.frase}, é palíndromo')
#         else:
#             print(f'A palavra ou frase {self.frase}, não é palíndromo')