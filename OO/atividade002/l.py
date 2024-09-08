#Faça um programa que verifique se o usuário e senha estão inseridos em um banco de dados (fake). 
# O usuário só terá acesso se digitar os dados corretos e, assim, sair do laço.
import os


class Login:
    def __init__(self, usuario, senha):
        self.usuario = usuario
        self.senha = senha
        
class VerificarLogin(Login):
    def verifica(self):
        while True:
            if (self.usuario == 'leonardo' and self.senha == '1234'):
                print('Acesso permitido, Bem-vindo')
                print()
                break
            else:
                print('Acesso negado')
                break


os.system('cls')

print('-' * 80)
print('USUÁRIO E SENHA')
print('=' * 80)

usuario = input('Entre com o usuário: ').lower()
senha = input('Entre com a senha: ')
verificar = VerificarLogin(usuario, senha)
verificar.verifica()
