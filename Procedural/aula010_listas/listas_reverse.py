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

#Exibe a lista fornecida para a referencia
print(f'Lista fornecida: {numeros}')

#Solicita ao usuário para decidir se deseja inverter a Lista
escolha = input('Deseja inverter a ordem da lista? (s/n): ').strip().lower()

#Verifica a escolha do usuario e inverte a lista se a resposta for 's'
if escolha == 's':
    numeros.reverse()
    print(f'Lista invertida {numeros}')
else:
    print(f'A lista não foi invertida')
