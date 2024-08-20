# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Leonardo Barbosa
# Data:
# Crie um programa que peça ao usuário 2 números maiores que 0 e menores que 11. # Depois mostre um menu com as seguintes operações:
# 1. Soma: 2. Subtração : 3. Produto : 4. Divisão : 4. Divisão inteira : 6.
# Resto da divisão.
# O usuário deverá escolher um número maior ou  igual a 1 e menor ou igual a 6.
# Em seguida, você criará funções que retornem os resultados das operações
# imprimindo os resultados na tela.
import os


os.system('cls')

while True:
    numero_1 = int(
        input('Entre com o primeiro número maior que 0 e menor que 11...: '))
    numero_2 = int(
        input('Entre com o segundo número maior que 0 e menor que 11....: '))
    print()

    if (numero_1 <= 0 or numero_1 >= 11) or (numero_2 <= 0 or numero_2 >= 11):
        print('Número fora do intervalo solicitado. Digite novamente!!')
        input('Continue...')
        os.system('cls')

    else:
        print('--OPERAÇÕES--')
        opcao = input('1. Soma\n'
                      + f'2. Subtração\n'
                      + f'3. Pruduto\n'
                      + f'4. Divisão\n'
                      + f'5. Divisão inteira\n'
                      + f'6. Resto\n\n')

        if opcao == '1':
            def soma(numero1, numero2):
                resultado = numero1 + numero2
                return resultado
            somar = soma(numero_1, numero_2)
            print(f'{numero_1} + {numero_2} = {somar}')
            print()
            input('Continue...')
            print()
            os.system('cls')

        elif opcao == '2':
            def subtracao(numero1, numero2):
                resultado = numero1 - numero2
                return resultado
            subtrair = subtracao(numero_1, numero_2)
            print(f'{numero_1} - {numero_2} = {subtrair}')
            print()
            input('Continue...')
            print()
            os.system('cls')

        elif opcao == '3':
            def produto(numero1, numero2):
                resultado = numero1 * numero2
                return resultado
            multiplicar = produto(numero_1, numero_2)
            print(f'{numero_1} × {numero_2} = {multiplicar}')
            print()
            input('Continue...')
            print()
            os.system('cls')

        elif opcao == '4':
            def divisao(numero1, numero2):
                resultado = numero1 / numero2
                return resultado
            dividir = divisao(numero_1, numero_2)
            print(f'{numero_1} ÷ {numero_2} = {dividir}')
            print()
            input('Continue...')
            print()
            os.system('cls')

        elif opcao == '5':
            def divisao_inteira(numero1, numero2):
                resultado = numero1 // numero2
                return resultado
            dividir_inteiro = divisao_inteira(numero_1, numero_2)
            print(f'A divisão inteira de: {numero_1} ÷ '
                  + f'{numero_2} = {dividir_inteiro}')
            print()
            input('Continue...')
            print()
            os.system('cls')

        elif opcao == '6':
            def resto(numero1, numero2):
                resultado = numero1 % numero2
                return resultado
            resto_divisao = resto(numero_1, numero_2)
            print(f'O resto da divião de: {numero_1} ÷ '
                  + f'{numero_2} = {resto_divisao}')
            print()
            input('Continue...')
            print()
            os.system('cls')

        elif opcao > '6':
            finalizar = input(
                'Opção inválida, deseja finalizar o programa? [s - n] ').lower()
            if finalizar == 's':
                print('Programa finalizado!!!')
                print()
                break
            else:
                os.system('cls')
