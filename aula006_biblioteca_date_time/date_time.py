#Importando as bibliotecas
import os
#Podemos importar só as funções que queremos utilizar
from datetime import datetime
from datetime import date


#Limpando o terminal
os.system('cls')

#Declarando uma variável para data
data = datetime.now()

#Declarando uma variável data formatada
data_formatada = data.strftime('%d/%m/%Y')

#Declarando uma variável data e hora formatada
data_hora_formatada = data.strftime('%d/%m/%Y %H:%M')

print(f'Data formatada: {data_formatada}')
print(f'Data e hora formatadas: {data_hora_formatada}')

#recebendo o ano
data_atual = date.today()
nascimento = 1970
idade = data_atual.year - nascimento

#Imprimindo a data atual e o nascimento
print('-' * 70)
print(f'Data atual no sistema: {data_atual}')
print(f'Nascimento...........: {nascimento}')
#Imprimindo só o ano
print(f'Ano atual............: {data_atual.year}')
#Imprimindo só a idade
print(f'Sua idade é..........: {idade} anos')
print('-' * 70)