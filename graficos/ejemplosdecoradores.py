def funcion_decoradora(funcion_parametro):
    def funcion_interior(*args):    #*args es decirle a python que puede recibir un numero indeterminado de parametros
#acciones adicionales que decoran
        print("Realizar calculos:")
        funcion_parametro()
        print("HA terminado el calculo")
    return funcion_interior()
@funcion_decoradora
def suma(num1, num2):
    print(num1+num2)
@funcion_decoradora
def resta(num1,num2):
    print(num1-num2)

suma(5,5)
resta(87,53)