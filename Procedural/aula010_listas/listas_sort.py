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
    
# Solicita ao usuário para escolher a ordem de classsificação
ordem = input('Digite "asc" para ordem ascendente ou "desc" para ordem descendente: ').strip().lower()

#Verifica a escolha do usuário e ordena a lista de acordo
if ordem == 'asc':
    numeros.sort()
    print(f'Lista ordenada em ordem ascendente: {numeros}')
elif ordem == 'desc':
    numeros.sort(reverse=True)
    print(f'Lista ordenada em ordem descendente: {numeros}')
else:
    print('Opção inválida! A lista não foi ordenada')

#Exibe a lista fornecida para referencia
print(f'Lista fornecida: , {numeros}')
