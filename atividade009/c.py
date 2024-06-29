# c)Utilizando o exercício anterior , retire um elemento do dicionário.
import os


os.system('cls')

print('-' * 70)
print('RETIRANDO 1 ELEMENTO DO DICIONÁRIO')
print('=' * 70)

cadastro = {}

# cadastro['nome'] = 'Leonardo'
# cadastro['idade'] = 28
# cadastro['endereco'] = 'Rua A'
# cadastro['cidade'] = 'Juiz de Fora'
# cadastro['pais'] = 'Brasil'
# cadastro['telefone'] = '9999-4040'


quantidade_itens = input('Quantos elementos deseja inserir? ')
quantidade_itens = int(quantidade_itens)

# QUANDO TEM UM RANGE NO FOR É UMA CONTAGEM
for c in range(quantidade_itens):
    print(f'Adicionando o elemento {c + 1}')
    print()
    chave = input('Entre com a chave: ')
    valor = input('Entre com o valor: ')
    cadastro[chave] = valor
    print()

# QUANDO NÃO TEM RANGE NO FOR VARREDURA
for chave, valor in cadastro.items():
    print(f'{chave.capitalize()}:{valor}', end=', ')
print()
print()

# apagar é a CHAVE, retirado é o VALOR
apagar = input('Qual elemento deseja apagar? ')
# O elemento não encontrado é um default
retirado = cadastro.pop(f'{apagar} Teste','Elemento não encontrado')
print(retirado)
print()
