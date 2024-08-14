import csv
import os


# Nome do arquivo CSV
arquivo = 'aula016_arquivos/arquivos_csv/gravacao/alunas.csv'

# Lista para armazenar os dados
lista = []

# Abrindo o arquivo CSV para leitura
with open(arquivo, 'r') as arquivo_csv:
    # Criando um leitor de CSV que lê o arquivo como dicionário
    leitura = csv.DictReader(arquivo_csv, delimiter=';')

    # Iterando sobre cada linha (registro) no arquivo CSV e adicioanando à lista
    for linha in leitura:
        lista.append(linha)

os.system('cls')
print('-' * 70)
print('nome\ttelefone\tcidade')
print('=' * 70)
# Exibindo
for registro in lista:
    flag = 0
    for v in registro.values():
        print(v, end='\t')
        flag += 1
        if flag == 3:
            print()
print('-' * 70)
