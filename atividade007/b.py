# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Leonardo Barbosa
# Data: 17/06/2024
# b)Após esta entrada de dados, faça o seguinte: • Mostre a quantidade de notas que foram lidas.
# • Exiba todas as notas na ordem em que foram informadas.
# • Exiba todas as notas na ordem inversa à que foram informadas, uma abaixo da outra.
# • Calcule e mostre a soma das notas. • Calcule e mostre a média das notas.

import os


os.system('cls')

print('-' * 80)
print('NOTAS, QUANTIDADE, SOMA E MÉDIA ')
print('=' * 80)

notas = []
entrada = ""
quantidade_notas = 0
soma = 0
media = 0

while entrada.lower() != 's' and entrada != '0':
  entrada = input('Digite uma nota: [0 ou s - Sair] ')
  notas.append(entrada)
  soma += int(entrada)

  if entrada.lower() == 's' or entrada == '0':
    print()
    print('Programa finalizado!!!')
    print()
    notas.pop()
    
media = soma / len(notas)
quantidade_notas = len(notas)
notas_inversas = notas[::-1]
print('-' * 80)
print(f'A quantidade de notas digitadas foram de {quantidade_notas} notas')
print()
print(f'As notas digitas foram: {notas}')
print()
print('As notas invertidas')
print('\n'.join(notas_inversas))
print()
print(f'Soma das notas: {soma}')
print()
print(f'Média das notas: {media}')
print()
