# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Leonardo Barbosa
# Data: 17/04/2024 
# Operadores Aritiméticos

#imports
import os

#limpar o terminal
os.system('cls')

print('_' * 70)
print('OPERADORES ARITIMÉTICOS')
print('=' * 70)

#Entrada de Dados
print ('--- SOMA')
print('-' * 70)
parcela_1 = float(input('Entre com a 1ª parcela: '))
parcela_2 = float(input('Entre com a 2ª parcela: '))

print()
print('--- SUBTRAÇÃO')
print('-' * 70)
minuendo = float(input('Entre com o minuendo: '))
subtraendo = float(input('Entre com o subtraendo: '))

print() #POSSO UTILIZAR O \n NA LINHA DE CIMA
print('--- PRODUTO')
print('-' * 70)
multiplicando = float(input('Entre com o multiplicando: '))
multiplicador = float(input('Entre com o multiplicador: '))

print()
print('--- DIVISÃO')
print('-' * 70)
dividendo = float(input('Entre com o dividendo: '))
divisor = float(input('Entre com o divisor: '))

print()
print('--- RAÍZES')
print('-' * 70)
radicando = float(input('Entre com um valor para calcular a raiz quadrada: '))
# indice = float(input('Entre com um ídice da raiz:')) #PARA CAUCULAR RAÍZES COM ÍNDICES DIFERENTES DE 2 E 3


#Processamento
soma = parcela_1 + parcela_2
diferenca = minuendo - subtraendo
produto = multiplicando * multiplicador
quociente = dividendo / divisor
raiz_quadrada = radicando ** (1/2)
raiz_cubica = radicando ** (1/3)
# raiz_n = radicando ** (1/indice)

#Saída
print('=' * 70)
print('RESULTADOS')
print('-' * 70)
print(f'A soma de {parcela_1} + {parcela_2} é: {soma}')
print(f'A subtração de {minuendo} - {subtraendo} é: {diferenca}')
print(f'A multiplicação de {multiplicando} x {multiplicador} é: {produto}')
print(f'A divisão de {dividendo} ÷ {divisor} é: {quociente}')#COLOCAR SINAL DE MULTIPLICAÇÃO ALT 0247
print(f'A raiz quadrada de {radicando} é: {raiz_quadrada}')
print(f'A raiz cúbica de {radicando} é {raiz_cubica}')
# print(f'A raiz de índice {indice} e de radicando {radicando} é: {raiz_n}')




