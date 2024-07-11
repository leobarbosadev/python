# import locale
# import os
# import datetime


# os.system('cls')

# data = datetime.datetime.now()

# locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')
# data_completa = data.strftime('%c')  # EXIBE A DATA COMPLETA
# mes = data.strftime('%B') # EXIBE O MÊS COMPLETO, %b EXIBE O MÊS ABREVIADO

# print(data_completa)
# print(mes)


# print('-' * 80)
# print('*** ESTRUTURA DE CONTROLE FOR RANGE COM VALIDAÇÃO E CASTING ***')
# print('=' * 80)

# for c in range(0, 5):
#     numero = input('Digite um número [0-5]: ')

#     # VALIDAÇÃO
#     if (not (numero.isnumeric())):
#         print(f'"{numero}" Entrada inválida')
#         print()
#     elif (int(numero) >= 0 and int(numero) <= 5):

#         print(f'O número {numero} está dentro do intervalo [0-5]!')
#         print()
#     else:
#         print(f'"{numero}" Entrada inválida!')
#         print()


# numero = 1
# contador = 0  # QTD DE MULTIPLICAÇÃO
# for c in range(0, 20):
#     if c % numero != 0:
#         numero +=1
#         contador += 1
#         print(c)
#     if contador == 2:
#         print(c)


# dicionario = {
#     'chave1': [1, 2, 3],
#     'chave2': ['a', 'b', 'c'],
#     'chave3': [True, False]
# }

# ---------- SET ----------
# set1 = {1, 2, 3}
# set2 = {1, 2, 3, 4, 5, 6}
# set3 = {3, 7, 8, 9}
# sub_conj = set1.issubset(set2)

# adicionar = set1.add(10)
# remover = set2.discard(5)
# set_juntos = set1.union(set2, set3)
# set_juntos2 = set1 | set2 | set3
# intersecao = set1.intersection(set2, set3)
# intersecao2 = set1 & set2 & set3
# simetrico = set1.symmetric_difference(set2)

# print(sub_conj) # RETORNA True OU False
# print(simetrico)
# print(intersecao)
# print(intersecao2)
# print(set1)
# print(set_juntos)
# # print(set_juntos2)

# ---------- DICIONÁRIO ----------
import random
import os


os.system('cls')

curiosidade1999 = ['Teste 1999', 'Teste 1999B', 'Teste 1999C']
curiosidade2000 = ['Teste 2000', 'Teste 2000B', 'Teste 2000C']
curiosidade2001 = ['Teste 2001', 'Teste 2001B', 'Teste 2001C']
curiosidade2002 = ['Teste 2002', 'Teste 2002B', 'Teste 2002C']

curiosidade_aleatoria1999 = random.choice(curiosidade1999)
curiosidade_aleatoria2000 = random.choice(curiosidade2000)
curiosidade_aleatoria2001 = random.choice(curiosidade2001)
curiosidade_aleatoria2002 = random.choice(curiosidade2002)

lista = [
    {'1999': curiosidade_aleatoria1999},
    {'2000': curiosidade_aleatoria2000},
    {'2001': curiosidade_aleatoria2001},
    {'2002': curiosidade_aleatoria2002},
]

entrada = input('Entre com seu ano de nascimento: ')
for i in lista:
    for chave in i:
        if entrada in chave:
            print(f'{i[entrada]}')


# curiosidade_aleatoria = random.choice(lista[0])
# print(curiosidade_aleatoria)

# Selecionar um dicionário aleatório da lista
# dicionario_aleatorio = random.choice(lista)

# Obter a chave e o valor do dicionário aleatório
# chave_aleatoria = list(dicionario_aleatorio.keys())[0]
# valor_aleatorio = dicionario_aleatorio[chave_aleatoria]

# Selecionar um dicionário aleatório da lista
# dicionario_aleatorio = random.choice(lista)

# Exibir o valor
# print(valor_aleatorio)


# #Funcao sem return é void
# def soma(a, b):
#     """_summary_

#     Args:
#         a (_type_): _description_
#         b (_type_): _description_

#     Returns:
#         _type_: _description_
#     """    
#     resultado = a + b
#     return resultado # CASO EU PASSAR ALGUM VALOR AQUI É ARGUMENTO




# for aluno in alunos:
    # print(f'Nome: {alunos['nome']}')


# def cadastrar_aluno():
#     alunos = []  # Lista para armazenar os dados dos alunos
    
#     # Loop para cadastrar os dados de três alunos
#     for i in range(3):  # Altere o número conforme necessário
#         print(f"Cadastro do aluno {i+1}:")
#         nome = input("Nome: ")
#         matricula = input("Matrícula: ")
#         data_nascimento = input("Data de Nascimento (DD/MM/AAAA): ")
        
#         # Criando um dicionário com os dados do aluno
#         aluno = {
#             'nome': nome,
#             'matricula': matricula,
#             'data_nascimento': data_nascimento
#         }
        
#         # Adicionando o aluno à lista de alunos
#         alunos.append(aluno)
        
#     return alunos

# def imprimir_alunos(alunos):
#     print("\nDados dos alunos cadastrados:")
    
#     # Iterando sobre a lista de alunos e imprimindo os dados
#     for aluno in alunos:
#         print(f"Nome: {aluno['nome']}")
#         print(f"Matrícula: {aluno['matricula']}")
#         print(f"Data de Nascimento: {aluno['data_nascimento']}")
#         print()  # Linha em branco para separar os dados de cada aluno

# # Testando a função
# alunos_cadastrados = cadastrar_aluno()
# imprimir_alunos(alunos_cadastrados)