# Faça um programa que verifique se o usuário e senha estão inseridos em um banco de dados (fake).
# O usuário só terá acesso se digitar os dados corretos e, assim, sair do laço.

import os


os.system('cls')

print('-' * 80)
print('USUÁRIO E SENHA')
print('=' * 80)


while True:
    usuario = input('Entre com o usuário: ').lower()
    senha = input('Entre com a senha: ')

    if (usuario == 'leonardo' and senha == '1234'):
        print('Acesso permitido, Bem-vindo')
        print()
        break
    else:
        print('Acesso negado')
        break
