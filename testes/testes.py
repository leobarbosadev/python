import locale
import os
import datetime


os.system('cls')

data = datetime.datetime.now()

locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')
data_completa = data.strftime('%c')  # EXIBE A DATA COMPLETA
mes = data.strftime('%B') # EXIBE O MÊS COMPLETO, %b EXIBE O MÊS ABREVIADO

print(data_completa)
print(mes)




print('-' * 80)
print('*** ENTRADA DE DADOS ***')
print('=' * 80)

for c in range(0, 5):
    numero = input('Digite um número [0-5]: ')

    # VALIDAÇÃO
    if (not (numero.isnumeric())):
        print(f'"{numero}" Entrada inválida')
        print()
    elif (int(numero) >= 0 and int(numero) <= 5):
        
        print(f'O número {numero} está dentro do intervalo [0-5]!')
        print()
    else:
        print(f'"{numero}" Entrada inválida!')
        print()