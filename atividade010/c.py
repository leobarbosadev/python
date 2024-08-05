# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Leonardo Barbosa
# Data:
# Crie uma função que verifica se uma aluno(a) está cadastrado ou não em um dicionário.
# Se estiver cadastrado, imprima o nome desse aluno e o resto dos seus dados.
# O dicionário deverá conter nome, matrícula e a data de nascimento do aluno.

import os


os.system('cls')


dicionario_aluno = {'nome': 'Leonardo', 'matricula': '0011AB', 'nascimento': '03/09/1995'}


def verificar_aluno():
    if dicionario_aluno['nome'] == 'Leonardo':
        for chave, valor in dicionario_aluno.items():
            print(f'{chave}: {valor}')
    else:
        print(f'Nome não encontrado no dicionário {dicionario_aluno['nome']}')

verificar_aluno()
