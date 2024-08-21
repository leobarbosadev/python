import os


class Carro:
    def __init__(self, marca, modelo, ano, cor): # MÉTODO CONSTRUTOR
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        
# Solicitando entrada de dados do usuário
os.system('cls')
print('-' * 70)
marca = input('Digite a marca do carro: ')
modelo = input('Digite o modelo do veículo: ')
ano = int(input('Digite o ano do carro: '))
cor = input('Digite a cor do carro: ')

# Criando um objeto da classe Carro com dados fornecidos pelo usuário
carro1 = Carro(marca, modelo, ano, cor)

# Acessando e imprimindo atributos do objeto
print('-' * 70)
print('\nInformações do Veículo:') # \n QUEBRA UMA LINHA ANTES - DA UM ESPAÇO A MAIS
print('=' * 70)
print(f'Marca: {carro1.marca}')
print(f'Modelo: {carro1.modelo}')
print(f'Ano: {carro1.ano}')
print(f'Cor: {carro1.cor}')
print('-' * 70)