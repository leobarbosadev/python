def limpa_tela():  # DEFINIÇÃO DE FUNÇÃO
    """FUNÇÃO PARA LIMPAR O TERMINAL
    """
    import os
    os.system('cls')


# Funcao sem return é void
def soma(a, b): # ISSO SÃO PARÂMETROS
    """FUNÇÃO PARA SOMAR 2 NÚMEROS # DOCSTRING

    Args:
        a (int): Valor de a
        b (int): Valor de b

    Returns:
        Retorna a soma de 2 números
    """
    return a + b


def firula():
    print('-' * 70)

# Programa principal


# Chamando a Função
limpa_tela() # CASO EU PASSAR ALGUM VALOR AQUI É ARGUMENTO
firula()
resposta = soma(1, 2)  # INVOCANDO UMA FUNÇÃO (ISSO É UM RETORNO DIRETO)
print(f'A soma dos 2 números é: {resposta}')
firula()
print()
