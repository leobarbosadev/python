# Evolua o programa anterior para um código que pergunte ao usuário qual o
# intervalo que ele deseja ver  impresso.
import os


class Intervalo:
    def __init__(self, inicio, fim):
        self.inicio = inicio
        self.fim = fim


class ExibirIntervaloEntreNumeros(Intervalo):
    def exibir(self):
        for c in range(self.inicio, self.fim + 1):  # for c in range(0, 100)
            print(f'{c}', end=' | ')  # print(f'{c + 1}', end=',')


os.system('cls')
inicio = int(input('Entre com um número inicial: '))
fim = (int(input('Entre com um número final: ')))
print('-' * 80)
print(f'*** DE 1 ATÉ {fim} ***')
intervalo = ExibirIntervaloEntreNumeros(inicio, fim)
intervalo.exibir() # QUANDO TEMOS UM PRINT DENTO DO METODO, NÃO PRECISO ATRIBUIR O METODO A UMA VARIAVEL.
print()
print('=' * 80)
print()
