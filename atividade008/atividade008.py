# Trabalho sobre a estrutura de dados SET
# SENAC Minas Gerais/Juiz de Fora
# Aluno: Leonardo Barbosa e Silva
# Turma: 0152
# Ano: 2024

# add(elemento): Adiciona um elemento ao set.

import os


os.system('cls')

# Solicita ao usuário a quantidade de itens que vai ser inserido
quantidade_itens = int(input('Quantos itens deseja adicionar? '))

# Criando um conjunto vazio
conjunto_numeros = set()

# Entrada de 

while True:
    print('Utilizando o método ADD()')
    # Adicionando valores a lista com uma entrada
    
    numero = int(input('Entre com um número [0 - sair]: '))
    conjunto_numeros.add(numero)
    os.system('cls')

    for i in range(numero):
        print(f'Os núemros adicionados foram: {numero}')
        break
