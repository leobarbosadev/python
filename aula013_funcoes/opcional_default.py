import os


os.system('cls')


# Definiçao da função
def multiplicar(a, b=1):  # VALOR DEFAULT, SE NENHUM VALOR FOR ATRIBUÍDO A b ELE VALERÁ 1
    return a * b

resultado_1 = multiplicar(5)
resultado_2 = multiplicar(5, 2)

print(f'Primeiro resultado: {resultado_1}')
print(f'Segundo resultado.: {resultado_2}')
print()
