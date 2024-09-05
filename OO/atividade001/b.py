# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Leonardo Barbosa
# Data: 02/09/2020
# Faça um programa que peça o ano do seu nascimento e calcule a sua idade.
import os
import datetime


class Verificar_idade:
    def __init__(self, ano_nascimento):
        self.ano_nascimento = ano_nascimento

    def calcular_idade(self):  # TEM QUE INICIAR SEMPRE COM O SELF
        ano_atual = datetime.datetime.now().year
        idade = int(ano_atual) - self.ano_nascimento
        return idade, ano_atual  # Para passar o ano atual preciso retornar ano atual aqui


while True:
    os.system('cls')
    ano = int(input('Entre com seu ano de nascimento: '))
    idade = Verificar_idade(ano)
    # Para passar o ano atual preciso retornar ano atual aqui
    idade, ano_atual = idade.calcular_idade()
    # Para passar o ano atual
    input(f'Sua idade no ano {ano_atual} é de {idade}')
    break
