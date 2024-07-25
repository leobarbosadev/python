# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Leonardo Barbosa
# Data:
# Uma Academia deseja fazer uma pesquisa entre seus clientes para
# descobrir a média de altura  e peso de seus clientes.
# Faça um programa que pergunte a cada um dos clientes da academia seu código
# nome, altura e peso. Após esse cadastramento, seu programa deverá listar
# os dados dos clientes e a média. Para sair do programa o usuário
# deverá digitar o valor zero(0). O número de clientes é indefinido.
import os


os.system('cls')


soma_peso = 0
soma_altura = 0

def media_altura_peso():
    for aluno in clientes:
        soma_altura += aluno['altura']
        soma_peso += aluno['peso']
    media_altura = soma_altura / len(clientes)
    media_peso = soma_peso / len(clientes)
    return media_altura, media_peso
    


clientes = []

while True:
    media_altura, media_peso  = media_altura_peso()
    codigo = int(input("Digite o código do cliente (ou '0' para terminar): "))
    if codigo == 0:
        break
    
    nome = input("Digite o nome do cliente: ")
    altura = float(input("Digite a altura do cliente: "))
    peso = float(input("Digite o peso do cliente: "))
    # print('Cliente cadastrado com sucesso')
    os.system('cls')
    cliente = {'codigo': codigo,'nome': nome,'altura': altura,'peso': peso}
    clientes.append(cliente)
    
print("\nLista de Clientes:")
# for cliente in clientes:
#     print(f"Código: {cliente['codigo']}")
#     print(f"Nome: {cliente['nome']}")
#     print(f"Altura: {cliente['altura']} metros")
#     print(f"Peso: {cliente['peso']} kg")

for cliente in clientes:
    for chave, valor in cliente.items():
        print(f'{chave}: {valor}', end= ' | ')
    print()
print()
print(f'Média altura: {media_altura}')
