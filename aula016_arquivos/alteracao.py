import csv
import os


os.system('cls')

arquivo = 'aula016_arquivos/arquivos_csv/gravacao/alunas.csv'
nome_existente = input('Digite o nome que deseja alterar: ')
novo_nome = input('Digite o novo nome: ')

with open(arquivo, 'r') as arquivo_csv:
    leitura = csv.DictReader(arquivo_csv, delimiter=';')
    cadastro = list(leitura)
print(cadastro)    

alterado = False
for registro in cadastro:
    if registro['nome'] == nome_existente:
        registro['nome'] = novo_nome
        alterado = True

if alterado:
    with open(arquivo, 'w', newline='') as arquivo_csv:
        campos = ['nome', 'telefone', 'cidade']
        escrever = csv.DictWriter(
            arquivo_csv, fieldnames=campos, delimiter=';')

        escrever.writeheader()
        escrever.writerows(cadastro)
    print(f'Registro com nome {novo_nome} alterado com sucesso.')
else:
    print(f'{novo_nome} não encontrado.')

print(cadastro)