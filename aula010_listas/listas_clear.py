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

#Exibe a lista fornecida para referencia
print(f'Lista fornecida {numeros}')

#Solicita ao ususario para decidir se deseja limpar a lista
escolha = input('Deseja limpar a lista? (s/n): ').strip().lower()

#Verifca a escolha do usuário e cria uma copia da lista se a resposta for 's'
if escolha == 's':
    lista_copiada = numeros.()
    print(f'Copia da lista {lista_copiada}')
else:
    print('A lista não foi copiada')
