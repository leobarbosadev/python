def teste(a, b, c):
    a = a + 1
    b += 1
    c += 1

    return a, b, c


# Invovando
valor1, valor2, valor3 = teste(10, 10, 10)

print(valor1)
print(valor2)
print(valor3)
