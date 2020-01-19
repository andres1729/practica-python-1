print("Calculo de raiz cuadrada")
numero = int(input("Introduce numero "))
import math
intentos = 0

while numero < 0:
    print("no se puede hallar la raiz cuadrada de un numero negativo")

    if intentos == 2:
        print("Has agotado los intentos. Fin del programa")
        break;

    numero = int(input("Introduce un numero "))
    if numero < 0:
        intentos = intentos + 1
if intentos < 2:
    solucion = math.sqrt(numero)
    print("La raiz cuadrada de" + str(numero) + "es " + str(solucion))
