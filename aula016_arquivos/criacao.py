# importar a biblioteca csv
import csv
import os


# criando uma lista de dicionários: cada dicionário é uma linha (registro)
lista = [
    {'nome':'Agata', 'telefone': '(32)98888-0000', 'cidade': 'Juiz de Fora'},
    {'nome': 'Bia', 'telefone': '(32)98888-1111', 'cidade':'Juiz de Fora'},
    {'nome': 'Coly','telefone': '(32)98888-2222', 'cidade': 'Juiz de Fora'},
    {'nome': 'Isis', 'telefone': '(32)98888-3333', 'cidade': 'Juiz de Fora'}
]

# Caminho para a pasta onde o arquivo CSV será salvo
pasta = 'aula016_arquivos/arquivos_csv/gravacao/'

# Verificando se a pasta exisite, se não, irá criá-la
os.makedirs(pasta, exist_ok=True)

# nome para o arquivo CSV para gravar as informações
arquivo = 'aula016_arquivos/arquivos_csv/gravacao/alunas.csv'

# Caminho completo do arquivo CSV
caminho_arquivo = os.path.join(pasta, arquivo)

# Abre o arquivo 'arquivo' no modo de escrita ('w')
# Se o arquivo não existir, ele será criado; se exixstir, será truncado (esvaziado).
# newline = '': Evita a adição de linhas em branco extras ao gravar o arquivo em algumas plataformas.
# os arquivos_csv: Atribui o objeto arquivo ao 'arquivo_csv' para ser usado dentro do bloco with.
with open(arquivo, 'w', newline='') as arquivo_csv:
    
    # campos = ['name', 'telefone', 'cidade']: Define a lista de nomes de campos
    # (cabeçalhos das colunas do CSV).
    campos = ['nome', 'telefone', 'cidade']

# writer = csv.DictWriter(arquivo_csv, fieldnames=campos):
# cria um objeto DictWriter que usará 'arquvio_csv' para gravar os campos.
# fileldnames define a ordem dos campos no arquivo CSV.
# delimiter = ';' é o separador
    escrever = csv.DictWriter(arquivo_csv, fieldnames=campos, delimiter=';')
    
    # write.writeheader(): Grava a linha do cabeçalho no
    # arquivo CSV usando os nomes de campos definindo em fieldnames.
    escrever.writeheader()
        
    # writer.writerows(lista): Gravar todas as linhas da lista no rquivo CSV
    # Cada dicionário em 'lista' se torna uma linha no arquivo.
    escrever.writerow(lista)
    
os.system('cls')
# Exibe uma mensagem indicando que o arquivo foi gravado com sucesso.
print(f'Arquivo {arquivo} graado com sucesso!')