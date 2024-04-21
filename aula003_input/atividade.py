# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Leonardo Barbosa
# Data: 17/04/2024
# Atividade de template string

# imports
import os

#Inferência
trabalho = False

os.system('cls')

print('-' * 100)
print('INSIRA OS DADOS')
print('=' * 100)

#Entrada com Casting
nome = str(input('Coloque seu nome aqui: '))
idade = int(input('Entre com sua idade: '))
peso = float(input('Entre com seu peso: '))
trabalho = True
# trabalho = bool(input('Está trabalhando no momento?(Coloque true para sim'
#                       + 'e false para não):'))
pais = str(input('Em que país você nasceu? '))

#Saída com template string
print('-' * 100)
print(f'Olá {nome}, você tem {idade} anos, pesa {peso} quilos,'
      + f'nasceu no país {pais} e trabalhando no momento: {trabalho}')
print('-' * 100)

#Saída com tipo de variáveis
print('A variável nome é do tipo---------', type(nome))
print('A variável idade é do tipo--------', type(idade))
print('A variável peso é do tipo---------', type(peso))
print('A variável pais é do tipo---------', type(pais))
print('A variável trabalho é do tipo-----', type(trabalho))
print('-' * 100)
print('')