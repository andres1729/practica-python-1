def multiplos_de(n):
    index = 1
    while True:
        yield index*n
        index = index + 1


if __name__ == '__main__':
    # En este caso genera múltiplos de 7
    for i in multiplos_de(7):
        print (i)

    # Bastaría usar multiplos_de(5) para múltiplos de 5
    # O multiplos_de(10) para generar múltiplos de 10