import os


os.system('cls')

# Inicializa a lista vazia
lista_numero = [3, 5, 7]

# Solicita ao usuário para inserir números separados por espaço
entrada = input('Digite números separados por espaço: ')

# Divide a string de entrada em uma lista de strings
numeros = entrada.split()

# Cria uma lista para armazenar os números pares
pares = []

# Itera sobre os números inseridos
for numero in numeros:
    # Converte a string para inteiro
    numero_aux = int(numero)
    # Verifica se o número é par
    if numero_aux % 2 == 0:
        # Adiciona o número par à lista de pares
        pares.append(numero_aux)

# Usa extend() para adicionar todos os números pares à lista principal
lista_numero.extend(pares)

# Exibe a lista resultante
print(f'Números pares adicionados à lista: {lista_numero}')
# Exibe a lista completa que foi digitada
print(f'Lista completa: {numeros}')
