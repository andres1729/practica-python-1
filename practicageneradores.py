# Definimos nuestra función
def pares():
    index = 1
    # En este caso definimos un bucle infinito
    while True:
        # Devolvemos un valor
        yield index*2
        index = index + 1


if __name__ == '__main__':
    # Para probarlo simplemente iteramos sobre la función
    for i in pares():
        print (i)