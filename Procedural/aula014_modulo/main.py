import os

from pacote.modulo_somar import somar
from pacote.subpacote.modulo_multiplicar import multiplicar as multi
from pacote.modulo_divisao import dividir

while True:
    os.system('cls')
    
    a = input('Entre com o valor de A: ')
    b = input('Entre com o valor de B: ')
    
    if not a.replace('.','',1).isdigit() or not b.replace('.','',1).isdigit():
        print('Por favor, entre com um número válido.')
        continue
    
    a = float(a)
    b = float(b)
    
    resultado_soma = somar(a, b)
    resultado_produto = multi(a, b)
    resultado_divisao, erro = dividir(a, b)
    
    print('-' * 70)
    print('CÁLCULOS MATEMÁTICOS')
    print('=' * 70)
    print(f'Cálculo da soma: {resultado_soma}')
    print(f'Cálculo do produto: {resultado_produto}')
    print(f'Cálculo da divisão: {resultado_divisao}, {erro}')
    print('-' * 70)
    
    sair = input('Deseja sair do programa? (s/n): ').strip().lower()
    if sair == 's':
        print('Saindo do programa...')
        break