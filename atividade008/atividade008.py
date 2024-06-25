# Trabalho sobre a estrutura de dados SET
# SENAC Minas Gerais/Juiz de Fora
# Aluno: Leonardo Barbosa e Silva
# Turma: 0152
# Ano: 2024

# add(elemento): Adiciona um elemento ao set.

import os


os.system('cls')

# Criando um conjunto vazio
conjunto_numeros = set()

while True:
    print('Utilizando o método ADD()')
    print()

    # Solicita ao usuário a quantidade de itens que vai ser inserido
    quantidade_itens = input('Quantos itens deseja adicionar? ')

    # Validando a quantidade_itens para entrar somente com número inteiro
    if (quantidade_itens == '') or not (quantidade_itens.isnumeric()):
        quantidade_itens = 0
    else:
        quantidade_itens = int(quantidade_itens)

    for item in range(quantidade_itens):
        # Adicionando valores a lista com uma entrada
        item = int(input(f'Entre com um o {item + 1}º número: '))
        conjunto_numeros.add(item)

    print('Os itens presentes no conjunto são: ')
    for item in conjunto_numeros:
        print(item, end=' | ')
    print()
    print()
    
    continuar = input('Deseja finalizar o programa? (s/n)')
    if continuar == 's':
        os.system('cls')
        break
    else:
        os.system('cls')
