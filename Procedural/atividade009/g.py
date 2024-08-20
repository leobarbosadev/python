# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Leonardo Barbosa
# Data: 01/07/2024
#g) Faça um programa para cadastrar os alunos de uma escola. Para os campos,
# tome como referência o nome do aluno, data de nascimento e matrícula.
import os


os.system('cls')

alunos = {}
lista_alunos = []
quantidade_alunos = input('Quantos alunos deseja cadastras? ')
quantidade_alunos = int(quantidade_alunos)

# CONTAGEM
for c in range(quantidade_alunos):
    print('-' * 70)
    print('DICIONÁRIO DE ALUNOS')
    print('=' * 70)
    print(f'Adicionando o {c + 1}º aluno') # c + 1 É PARA COMEÇAR A CONTAGEM EM 1
    alunos['nome'] = input('Entre com o nome do aluno..............: ')
    alunos['data_nascimento'] = input('Entre com a data de nascimento do aluno: ')
    alunos['matricula'] = input('Entre com a matrícula do aluno.........: ')
    os.system('cls')
    
    # USO O append() e copy PARA ADICIONAR UMA CÓPIA DO DICIONÁRIO NA LISTA
    lista_alunos.append(alunos.copy())

print('-' * 70)
print('LISTA COM TODOS OS ALUNOS')
print('=' * 70)
for elemento in lista_alunos: # PARA CADA ELEMENTO NA LISTA
    for chave, valor in elemento.items(): # PARA CADA CHAVE E VALOR NO DICIONÁRIO
        print(f'{chave}:{valor}', end=' | ')
    print()
print()
    