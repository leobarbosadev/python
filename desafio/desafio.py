# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Leonardo Barbosa
# Data: 17/06/2024
# Desafio
# Criar um código para exemplificar um CRUD, não é permitido funções ou validações try exception

#FAZER MAIS VALIDAÇÕES, TENTAR FAZER OPÇÕES 3 E 4 PELO ÍNDICE
import os


os.system('cls')

print('-' * 80)
print('EXEMPLO DE CRUD')
print('=' * 80)

nomes = []

# Loop principal do programa
while True:
    # print("\nMenu:")
    # print("1. Criar nome")
    # print("2. Mostrar todos os nomes")
    # print("3. Atualizar nome")
    # print("4. Deletar nome")
    # print("5. Sair")
    # opcao = input("Escolha uma opção (1-5): ")
    
    opcao = input("Escolha uma opção (1-5)\n"
    + f"1. Criar nome\n"
    + f"2. Mostrar todos os nomes\n"
    + f"3. Atualizar nome\n"
    + f"4. Deletar nome\n"
    + f"5. Sair\n\n")
    # Criar nome (C - CREATE)
    if opcao == '1':
        print()
        nome = input('Digite um nome: ').capitalize()
        nomes.append(nome)
        print('Nome adicionado') # NÃO EXIBE APÓS ADICIONAR O NOME
        os.system('cls')

    # Ler todos os nome  (R - READ)
    elif opcao == '2':
      for nome in nomes:
        print(nome, end=' | ')
      print()
      print()
        # print(f'Nomes cadastrados: {nomes}')

    # Atualizar nome (U - UPDATE)
    elif opcao == '3':
      # for indice, nome in enumerate(nomes, start= 1):
        # print(f'Codigo nome: {indice} = {nome}')
      print(nomes)
      nome_atualizar = input('Escolha um nome para atualizar: ').capitalize()
      if nome_atualizar in nomes:
        novo_nome = input('Digite o novo nome: ').capitalize()
        indice = nomes.index(nome_atualizar)
        nomes[indice] = novo_nome
        print('Nome atualizado')
    
    # Apagar nome (D - DELETE)
    elif opcao == '4':
      for nome_apagar in nomes:
        print(nome_apagar, end=', ')
      nome_apagar = input('\nDigite um nome para apagar: ').capitalize()
      if nome_apagar in nomes:
        nomes.remove(nome_apagar)
        print('Nome apagado')
    elif opcao == '5':
      print('Programa finalizado!!')
      break