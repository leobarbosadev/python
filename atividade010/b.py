# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Leonardo Barbosa
# Data:
# Crie uma função que cadastre o nome de uma aluno, a matrícula e a data de nascimento.
# Depois imprima os resultados cadastrados utilizando uma estrutura de repetição for.
import os


os.system('cls')

lista = []
def cadastrar_aluno(nome, matricula,data_nascimento):
    
    dicionario_aluno = {}
    
    dicionario_aluno['nome'] = nome
    dicionario_aluno['matricula'] = matricula
    dicionario_aluno['data_nascimento'] = data_nascimento
    
    lista.append(dicionario_aluno)
    
    for i in lista:
        for chave, valor in dicionario_aluno:
            print(f'{chave}:{valor}')
    
cadastro = dict(nome='Joao', matricula='002233', data_nascimento='10/03/1974')
print(cadastrar_aluno(**cadastro))



