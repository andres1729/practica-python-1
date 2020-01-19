i = 0

a = int(input("valor"))
while i <= a:
    print("Ejecucion" + str(i))
    i = i + 1
    #debe tener una condicion que en un momento determinado pase de ser verdadera a ser falss. Si no se hace tendremos un bucle infinito como ocurre al ejecutar este codigo. Tal condicion podria ser i = i+1
print("termino ejecucion" )