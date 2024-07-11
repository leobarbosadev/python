import os


os.system('cls')

# Definindo uma função


def calcular_velocidade_media(distancia, tempo):
    # Vm = deltaS/deltat

    if distancia < 1000:
        divide_distancia = 1
    else:
        divide_distancia = distancia / 1000

    if tempo < 60:
        divide_tempo = 1
    else:
        divide_tempo = tempo / 60

    velocidade_media = (distancia / divide_distancia) / (tempo / divide_tempo)

    return velocidade_media


distancia = float(input('Dgite a distância percorrida (em KM): '))
tempo = float(input('Digite o tempo gasto (em horas): '))

# Calcular a velocidade média usando a função criada
velocidade = calcular_velocidade_media(distancia, tempo)

# Exibir o resultado
print(f'A velociade média é {velocidade:.2f} km/h.')

# Se o usuario digitar minutos e metros?
