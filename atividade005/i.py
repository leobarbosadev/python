# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Leonardo Barbosa
# Data: 03/06/2024
#Faça um algoritmo que imprima a frase "estou em looping" e, em seguida, 
# solicite ao usuário digitar uma letra. 
# Caso a letra seja o “f" finalize a aplicação. 
# Do contrário, imprima novamente a mesma frase até que o caractere “f" seja digitado.

import os


os.system('cls')

print('-' * 80)
print('*** ESTOU EM LOOPING ***')
print('=' * 80)

while (True):
    frase = input('Estou em Looping... digite uma letra [f - Finalizar]: ').lower()
    
    if frase != 'f':
        frase = ('Estou em Looping... digite uma letra [f - Finalizar]: ')
    else:
        print('Aplicação finalizada\n')
        break
print('-' * 80)
print()