Método count()


# import os


# os.system('cls')

#Solicita ao usuário para inserir números separados por espaço
entrada = input('Diigite números separados por espaços: ')

#Divide a string de entrada em uma lista de strings
numeros_str = entrada.split()

#Converte a lista de strings e uma lista de inteiros
numeros = []
for num_str in numeros_str:
    numeros.append(int(num_str))

#Solicita ao usuário para inserir o número que deseja contar na lista
numero_para_contar = int(input('Digite o número que deseja contar: '))

#Conta o número de vezes que o número fornecido aparece na lista
contagem = numeros.count(numero_para_contar)

if contagem > 0:
    print(f'O número {numero_para_contar} aparece {contagem} vezes na lista.')
else:
    print(f'O número {numero_para_contar} não aparece na lista')

#Exibe a lista fornecida para referencia
print(f'Lista fornecida: {numeros}')
