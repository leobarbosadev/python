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
# maior = float()
# menor = float()
resposta = ''

if numero1 > numero2 > numero3:
    resposta = (f'O número {numero1} é maior que os número {numero2} e {numero3} '
    + f'e o número {numero3} é o menor deles')
# elif numero2 > numero3 and numero3 > numero1:
#     resposta = (f'O número {numero2} é maior que os número {numero1} e {numero3} '
#     + f'e o número {numero1} é o menor deles')
# elif numero3 > numero2 and numero2 > numero1:
#     resposta = (f'O número {numero3} é maior que os número {numero1} e {numero3} '
#     + f'e o número {numero1} é o menor deles')
else:
    resposta = f'Todos são iguais'
    
print('-' * 80)
print(resposta)
print()