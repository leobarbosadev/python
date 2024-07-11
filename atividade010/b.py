# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Leonardo Barbosa
# Data: 
#Crie uma função que cadastre o nome de uma aluno, a matrícula e a data de nascimento. 
# Depois imprima os resultados cadastrados utilizando uma estrutura de repetição for.
import os


os.system('cls')

def cadastrar_aluno(nome, matricula, data_nascimento):
    alunos = []
    for i in range(1):
        print(f'Cadastro do {i+1}º aluno:')
        nome = input('Entre com um nome: ')
        matricula = input('Entre com a matrícula: ')
        data_nascimento = input('Entre com a data de nascimento: ')
        
        aluno = {
            'Nome' : nome,
            'Matricula' : matricula,
            'data_nascimento': data_nascimento
        }
        alunos.append(aluno)
        
    return alunos

print()

