# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Leonardo Barbosa
# Data:
# Faça um programa de perguntas e respostas sobre os estados e capitais
# brasileiras. O programa deverá exibir para o usuário o estado e perguntar
# qual a sua capital. Se o usuário errar a resposta, o programa será finalizado
# apresentando quantas perguntas estão corretas.
# Utilize ao menos uma função e não há a necessidade de modularizar o código.
import os
import random

os.system('cls')

estados = [
    {'estado': 'Acre', 'capital': 'Rio Branco'},
    {'estado': 'Alagoas', 'capital': 'Maceió'},
    {'estado': 'Amapá', 'capital': 'Macapá'},
]


def verificar_capital():
    random.shuffle(estados)# ESCOLHO UM DICIONÁRIO ALEATÓRIO
    for i in estados: # VARREDURA NA LISTA
        estado_aleatorio = i['estado']# EXIBE SOMENTE O ESTADO DAQUELE DICIONÁRIO
        capital_correta = i['capital']# EXIBE SOMENTE A CAPITAL DAQUELE DICIONÁRIO
    
    return estado_aleatorio, capital_correta

acertos = 0
while True:
    estado_aleatorio, capital_correta = verificar_capital()
    print(f'O estado é: {estado_aleatorio}')
    resposta = input('Qual a capital desse estado? ').lower()

    if resposta == capital_correta.lower():
        print('Acertou!!!')
        acertos += 1
        print()
        
    else:
        print('Errou!!!')
        print()
        print(f'Você acertou {acertos} capitais')
        break
