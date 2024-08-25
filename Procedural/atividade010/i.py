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
    {'estado': 'Acre', 'capital': 'Rio Branco0'},
    {'estado': 'Alagoas', 'capital': 'Maceió'},
    {'estado': 'Amapá', 'capital': 'Macapá'},
    {'estado': 'Amazonas', 'capital': 'Manaus'},
    {'estado': 'Bahia', 'capital': 'Salvador'},
    {'estado': 'Ceará', 'capital': 'Fortaleza'},
    {'estado': 'Distrito Federal', 'capital': 'Brasília'},
    {'estado': 'Espírito Santo', 'capital': 'Vitória'},
    {'estado': 'Goiás', 'capital': 'Goiânia'},
    {'estado': 'Maranhão', 'capital': 'São Luís'},
    {'estado': 'Mato Grosso', 'capital': 'Cuiabá'},
    {'estado': 'Mato Grosso do Sul', 'capital': 'Campo Grande'},
    {'estado': 'Minas Gerais', 'capital': 'Belo Horizonte'},
    {'estado': 'Pará', 'capital': 'Belém'},
    {'estado': 'Paraíba', 'capital': 'João Pessoa'},
    {'estado': 'Paraná', 'capital': 'Curitiba'},
    {'estado': 'Pernambuco', 'capital': 'Recife'},
    {'estado': 'Piauí', 'capital': 'Teresina'},
    {'estado': 'Rio de Janeiro', 'capital': 'Rio de Janeiro'},
    {'estado': 'Rio Grande do Norte', 'capital': 'Natal'},
    {'estado': 'Rio Grande do Sul', 'capital': 'Porto Alegre'},
    {'estado': 'Rondônia', 'capital': 'Porto Velho'},
    {'estado': 'Roraima', 'capital': 'Boa Vista'},
    {'estado': 'Santa Catarina', 'capital': 'Florianópolis'},
    {'estado': 'São Paulo', 'capital': 'São Paulo'},
    {'estado': 'Sergipe', 'capital': 'Aracaju'},
    {'estado': 'Tocantins', 'capital': 'Palmas'}
]


def verificar_capital():
    random.shuffle(estados)  # ESCOLHO UM DICIONÁRIO ALEATÓRIO
    for i in estados:  # VARREDURA NA LISTA
        # EXIBE SOMENTE O ESTADO DAQUELE DICIONÁRIO
        estado_aleatorio = i['estado']
        # EXIBE SOMENTE A CAPITAL DAQUELE DICIONÁRIO
        capital_correta = i['capital']

    return estado_aleatorio, capital_correta


acertos = 0
while True:
    estado_aleatorio, capital_correta = verificar_capital()
    print(f'O estado é: {estado_aleatorio}')
    resposta = input('Qual a capital desse estado? ').lower()
    # os.system('cls')  # ASSIM FUNCIONA, MAS EXIBE O ACERTOU DEPOIS DE LIMPAR

    if resposta == capital_correta.lower():
        print('Acertou!!!')
        acertos += 1
        print()

    else:
        print('Errou!!!')
        print()
        print(f'Você acertou {acertos} capitais')
        break
