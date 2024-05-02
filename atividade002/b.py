# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Leonardo Barbosa
# Data: 26/04/2024
# B) A empresa "DataMax" está desenvolvendo um novo software de análise estatística e precisa de uma funcionalidade que permita aos usuários 
# inserir três números e, em seguida, exibir na tela qual é o maior número, qual é o menor número ou se os números são todos iguais. 
# Essa funcionalidade é crucial para os analistas de dados da "DataMax" que trabalham com conjuntos de dados diversos e precisam rapidamente 
# identificar as características básicas desses conjuntos, como a presença de outliers ou a uniformidade dos números.

import os


os.system('cls')

print('-' * 80)
print('Maior dos números')
print('-' * 80)

numero1 = int(input('Entre com o 1º número: '))
numero2 = int(input('Entre com o 2º número: '))
numero3 = int(input('Entre com o 3º número: '))
maior = float()
menor = float()

#Achar os maiores
if numero1 > numero2 and numero1 > numero3:
    maior = numero1
elif numero2 > numero1 and numero2 > numero3:
    maior = numero2
elif numero3 > numero2 and numero3 > numero1:
    maior = numero3

    
#Achar os menores
if numero1 < numero2 and numero1 < numero3:
    menor = numero1
elif numero2 < numero1 and numero2 < numero3:
    menor = numero2
elif numero3 > numero1 and numero3 < numero2:
    menor = numero3
else:
    resposta = f'Os números são iguais!!!'
    
print('-' * 80)
print(f'O maior número é: {maior} e o menor número é: {menor}')
print()