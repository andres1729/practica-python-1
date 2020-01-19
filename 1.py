#input significa entrada. Las entradas (inputs) son las señales o datos recibidos por el sistema
#Los calculos que ralizan las computadoras requieren para ser utiles la entrada de los datos necesarios para ejecutar las operaciensque posteriormente se convertiran en resutados
#Las operaciones de entrada permiten leer determinados valores y asignarlos a determinados variables.
nombre = input("cual es tu nombre?")
saludo = "hola,"
pregunta = "¿como estas hoy?"
print(saludo, nombre, pregunta)

lec = int(input("cuantas lecciones has vistos ?"))
total = 15
faltan = total-lec
print("Te faltan", faltan, "lecciones. Animo")

monedas = int(input("Cuantas monetas tienes?"))
siguiente = monedas + 1
print("yo tengo mas monedas", siguiente)

t= float(input("En cuantos segs corres 100m?"))
dif = t-9.58
print("Eres", dif, "segundos mas lentos que bolt")

ingreso = bool(input("ingresa tu nombre:"))
print("nombre ingresado", ingreso)
