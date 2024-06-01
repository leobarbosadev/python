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

import os 


os.system('cls')

print('SOMATÓRIO DE NÚMEROS PARES')
print()

a = int(input('Insira o menor número: '))
b = int(input('Insira o maior número: '))
print()

c = 0
soma = 0

for c in range(a, (b + 1), 2):
    numero = c
    
    soma += numero
    
    print(soma, end=' | ')