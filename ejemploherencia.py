
class Persona:
    # metodo constructor
    def __init__ (self, edad, nombre):
    #python requiere de la palabra self para acceder al resto de los metodos y atributos dentro de la clase
          self.edad = edad
          self.nombre = nombre
          print("se ha creado a", self.nombre, "de", self.edad)
#uso de metodos
    def hablar (self, palabras ):
        for frase in palabras:
          print(self.nombre, ':', frase)


class Deportista(Persona):

    def practicarDeporte(self):
          print(self.nombre, "Voy a practicar")


juan = Persona(30, "Juan")
juan.hablar("hola estoy hablando", "Este soy yo")
luis = Deportista(18, "Luis")
luis.hablar("Hola, estoy hablando ", "Este soy yo ")
luis.practicarDeporte()

