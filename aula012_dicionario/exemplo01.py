import os



os.system('cls')

#inicialização do dicionário e da lista
elementos = {}
periodica = []

#Entrada de dados
for c in range(2): # Considerando a entrada de 2 elementos
    print(f'Entrada de dados {c + 1}:')
    simbolo = str(input('Símbolo do elemento: '))
    nome = str(input('Nome do elemento: '))
    
    #Adiciona os dados ao dicionario
    elementos['simbolo'] = simbolo
    elementos['nome'] = nome
    
    #Usa append() com copy() para adicionar uma cópia do dicionario à lista
    periodica.append(elementos.copy())
    
print()
print('-' * 70)
print('Elementos na tabela periódica: ')
print(periodica)
print('-' * 70)
print()

#For aninhado para percorrer a lista e o dicionario
print('Detalhes dos elementos: ')
for elemento in periodica: # Para cada elemento (dicionario) na lista
    for chave, valor in elemento.items():
        print(f'{chave.capitalize()}: {valor}')
    print('-' * 70)