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


# numero = 1
# contador = 0  # QTD DE MULTIPLICAÇÃO
# for c in range(0, 20):
#     if c % numero != 0:
#         numero +=1
#         contador += 1
#         print(c)
#     if contador == 2:
#         print(c)


# dicionario = {
#     'chave1': [1, 2, 3],
#     'chave2': ['a', 'b', 'c'],
#     'chave3': [True, False]
# }
# set1 = {1, 2, 3}
# set2 = {1, 2, 3, 4, 5, 6}
# set3 = {3, 7, 8, 9}
# sub_conj = set1.issubset(set2)

# adicionar = set1.add(10)
# remover = set2.discard(5)
# set_juntos = set1.union(set2, set3)
# set_juntos2 = set1 | set2 | set3
# intersecao = set1.intersection(set2, set3)
# intersecao2 = set1 & set2 & set3
# simetrico = set1.symmetric_difference(set2)

# print(sub_conj) # RETORNA True OU False
# print(simetrico)
# print(intersecao)
# print(intersecao2)
# print(set1)
# print(set_juntos)
# # print(set_juntos2)

