#los generadores constituyen un determinado tipo de estructura que, a diferencia de lo que sucede con las funciones corrientes, no nos va a devolver un valor concreto, sino un objeto iterable cuyos resultados se van a ir generando uno a uno.

def devuelve_ciudades(*ciudades):
    for elemento in ciudades:
      #  for subElemento in elemento:
             yield from elemento


devuelve_ciudades=devuelve_ciudades("Madrid", "Barcelona", "Bilbao", "Valencia")
# Los elementos en el array esta compuesto por  subelementos. Podemos acceder de nuestra funcion generador a los elementos con bucles for anidados
print(next(devuelve_ciudades))

print(next(devuelve_ciudades))