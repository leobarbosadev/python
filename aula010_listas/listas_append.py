import os


os.system('cls')

# Inicializa uma lista vazia
lista_numeros = []

# Pede ao usuário para inserir três números
for i in range(3):
    numero = int(input('Digite um número: '))

    # Adiciona o número à lista
    lista_numeros.append(numero)

# Verifica se o número inserido está na lista e
# exibe uma mensagem correspondente
numero_verifica = int(input('Digite um número para verificar: '))

if numero_verifica in lista_numeros:
    print(f'O número {numero_verifica} está na lista!')
else:
    print(f'O número {numero_verifica} não está na lista.')
