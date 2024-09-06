import os


class Animal:
    def __init__(self, nome):
        self.nome = nome

    def latir(self):
        return 'Isto está no metodo latir()'

    def miar(self):
        return 'Isto está no metodo miar()'


# Herança CACHORRO HERDA DE ANIMAL
class Cachorro(Animal):
    def latir(self):
        return f'{self.nome} está latindo!'


# GATO HERDA DE ANIMAL
class Gato(Animal):
    def miar(self):
        return f'{self.nome} está miando'


os.system('cls')
cao = Cachorro('Rex')
gato = Gato('Tobias')
print(cao.latir())
print(gato.miar())
