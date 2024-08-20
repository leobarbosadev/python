# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Leonardo Barbosa
# Data:
# Crie uma função que cadastre o nome de um aluno, a matrícula e a data de nascimento.
# Depois imprima os resultados cadastrados utilizando uma estrutura de repetição for.
import os


os.system('cls')


def cadastrar_aluno(**aluno):
    for chave, valor, in aluno.items():
        print(f'{chave} : {valor}')
    print()


cadastrar_aluno(nome='Leonardo', matricula='0010AB', nascimento='03/09/1995')