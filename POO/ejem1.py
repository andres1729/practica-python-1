class coche():

    def __init__(self):
#Un constructor es un metodo especial que Python llama para instanciar un objeto usando las definiciones encontradas en tu clase. Python usa este constructor para crear tareas como la inicialización (asignar valores a variables), que se necesiten para iniciar. Los constructores tambien pueden verificar que tambien hay suficientes recursos para que el objecto desempeñe cualquier otra tarea para iniciar.
#Le nombre de constructor es siempre el mismo, por ejemplo __init__(). El constructor puede aceptar argumentos cuando es necesario crear objetos.
# Cada clase debe tener un constructur
       self.__largoChasis = 250
       self.__anchoChasis = 120              #propiedades de la clase
       self.__ruedas = 4
       self.__enmarcha = False

    #un metodo es una funcion especial que pertenece  a la clase creda y se escriben defs. En general son diferentes de las funciones
    #Las funciones definidas por def(en python, en otros lenguajes se llaman de otra forma, como function en PHP no pertenecen a una clase

    def arrancar(self, arrancamos):    # comportamiento
        self.__enmarcha = arrancamos
        if (self.__enmarcha):
            chequeo=self.__chequeo_interno()

        if(self.__enmarcha and chequeo):
            return "EL coche está en marcha"

        elif(self.__enmarcha and chequeo==False ):
            return "Algo ha ido mal en el chequeo. No podemos arrancar"

        else:
            return "el coche está parado"
        # La palabra self es una auto referencia y en general, en un método de instancia de un modelo, deberías usar self cuando modifiques atributos o cuando exista alguna ambigüedad entre llamar a una variable local y un atributo/método ya definido. Esto sucede en todos los lenguajes que usan POO y es una practica muy común y la mas correcta

       # pass impide que de error al ejecutar, por ello el metodo no hace nada si tiene pass

    def estado(self):
        print("El coche tiene ", self.__ruedas, "ruedas. Un ancho de ", self.__anchoChasis, "y un largo de", self.__largoChasis)

    def __chequeo_interno(self):
        print("realizando chequeo interno")

        self.gasolina = "ok"
        self.aceite = "ok"
        self.puertas = "cerradas"

        if(self.gasolina == "ok" and self.aceite == "ok" and self.puertas=="cerradas"):
            return True


micoche = coche()           #instanciar una clase (o crear un objeto de la clase ). no se utiliza el operador new presesnte en otros lenguajes de programacion
# El uso del punto (.) es para acceder a propiedades del objeto
print(micoche.arrancar(True))
micoche.estado()



print("---------A continuación creamos el segundo objeto------------")


micoche2 = coche()
 # El uso del punto (.) es para acceder a propiedades del objeto
print(micoche2.arrancar(False))
micoche2.estado()
