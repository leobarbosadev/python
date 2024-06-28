import os


os.system('cls')

meu_dicionario = {}

while True:
    print('-' * 70)
    print('\nMenu de opções:')
    print('1. Adicionar um par de chave-valor')
    print('2. Definir o valor padrão para uma chave usando setdefault()')
    print('3. Atulizar o dicionário usando update()')
    print('4. Mostrar dicionário atual')
    print('5. Sair')
    print('-' * 70)

    opcao = input('Escolha uma opção (1-5): ')

    if opcao == '1':
        # Adicionar um par de chave-valor ao dicionário
        chave = input('Digite a chave: ')
        valor = input('Digite o valor: ')
        meu_dicionario[chave] = valor
        print(f'par {chave} : {valor} adicionado')

    elif opcao == '2':
        # Definir valor padrão para uma chave usando setdefault()
        chave = input('Digite a chave para definir um valor padrão: ')
        valor_padrao = input('Digite o valor padrão: ')
        valor_existente = meu_dicionario.setdefault(chave, valor_padrao)
        print(f'Valor para a chave {chave} : {valor_existente}')

    elif opcao == '3':
        # Atualizar o dicionário usando update()
        # novos pares chave_valor no formato: chave1:valor1,chave2:valor2
        novos_pares = input('Digite os novos pares chave-valor'\
                            ' no formato chave1:valor1,chave2:valor2: ')
        novos_pares_lista = novos_pares.split(',')
        novos_dados = {}
        for par in novos_pares_lista:
            chave, valor = par.split(':')
            novos_dados[chave] = valor
        meu_dicionario.update(novos_dados)
        print(f'Dicionário atualizado: {meu_dicionario}')

    elif opcao == '4':
        # Mostrar o dicionário atual
        if meu_dicionario:
            print(f'Dicionário atual: {meu_dicionario}')
        else:
            print(f'O Dicionário está vazio.')

    elif opcao == '5':
        # Sai do programa
        print('Saindo do programa.')
        break
    else:
        # Mensagem para opção inválida
        print('Opção inválida. Tente novamente')
