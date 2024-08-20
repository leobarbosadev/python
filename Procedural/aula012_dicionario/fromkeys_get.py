import os


os.system('cls')

meu_dicionario = None

# Loop principal do programa
while True:
    print('-' * 70)
    # Exibição do menu de opções
    print('\nMenu de opções: ')
    print('1. Criar dicionário com fromkeys()')
    print('2. Buscar valor de uma chave com get()')
    print('3. Sair')
    print('-' * 70)
    
    opcao = input('Escolha uma opção (1-3): ')
    
    if opcao == '1':
        #Criação de um dicionário usando fromkeys()
        chaves = input('Digite as chaves separadas por vírgula: ').split(',') #Tipo Lista
        valor_padrao = input('Digite o valor padrão para as chaves: ')
        meu_dicionario = dict.fromkeys(chaves,valor_padrao)
        print(f'Dicionário criado: {meu_dicionario}')
    
    elif opcao == '2':
        #Verifica se o dicionário foi criado antes de tentar acessá-lo
        if meu_dicionario is not None:
            chave = input('Digite a chave que deseja buscar: ')
            valor = meu_dicionario.get(f'{chave} Chave não encontrada')
            print(f'Valor para a chave {chave}: {valor}')
        else:
            print('Erro! Crie um dicionário')
    
    elif opcao == '3':
        print('Saindo do programa.')
        break
    
    else:
        print('Opção inválida. Tente novamente.')