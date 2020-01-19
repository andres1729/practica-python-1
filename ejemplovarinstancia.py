
class Persona:
    # metodo constructor
    def __init__ (self, edad, nombre):
    #python requiere de la palabra self para acceder al resto de los metodos y atributos dentro de la clase
          self.edad = edad
          self.nombre = nombre
          print("se ha creado a", self.nombre, "de", self.edad)
#uso de metodos
    def hablar (self, palabras = "No se que decir"):
        print(self.nombre, ':', palabras)

juan = Persona(18, "Juan")
juan.hablar()
juan.hablar("hola, estoy hablando")
luis = Persona (20, "Luis")
luis.hablar("Hola estoy hablando ")
#uso de parametros especiales: para crear mas personas con diferentes nombres y edades debes modificar el constructor
# def __init__ (self):
#self.edad = 18
#self.nombre = "Juan"