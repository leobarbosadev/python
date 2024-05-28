import os


os.system('cls')

print('-' * 50)
print('ESTRUTURA DE CONTROLE SOMATÓRIO')
print('=' * 50)

print()

soma = 0 # É ITERNESSANTE SEMPRE QUE UMA VARIÁVEL RECBER UM CÁLCULO INICIALIZAR ELA COM 0

for var_iteradora in range(0, 4):
    numero = int(input(f'Digite o {var_iteradora + 1 }º número: ')) # O + 1 É PARA EXIBIR DE 1 A 4 E NÃO O ÍNDICE DE 0 A 3
    
    # CÁLCULO
    soma += numero # MESMA COISA QUE SOMA = SOMA + NUMERO
    
print('-' * 50)
print(f'A soma dos números é: {soma}')
print('-' * 50)
print()
