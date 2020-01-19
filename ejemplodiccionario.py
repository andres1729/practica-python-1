
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
        print(self.nombre, ':', palabras[frase])

juan = Persona(30, "Juan")
juan.hablar()
juan.hablar(t1 = "hola, estoy hablando", t2 = "Este soy yo")
luis = Persona (18, "Luis")
luis.hablar(t1 = "Hola estoy hablando ", t2 = "Este soy yo ")
#uso de parametros especiales: para crear mas personas con diferentes nombres y edades debes modificar el constructor
# def __init__ (self):
#self.edad = 18
#self.nombre = "Juan"