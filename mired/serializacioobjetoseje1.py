import pickle

class vehiculos():

    def __init__(self, marca,modelo):

        self.marca=marca
        self.modelo=modelo
        self.enmarcha=False
        self.acelera=False
        self.frena=False

    def arrancar(self):
         self.enmarcha=True

    def acelerar(self):
         self.acelera=True

    def frenar(self):
         self.frena=True

    def estado(self):
         print("Marca", self.marca, "\nmodelo:", self.modelo, "\En marcha:", self.enmarcha, "\nAcelerando:", self.acelera, "\nFrenando:", self.frena)

coche1=vehiculos("mazda", "mx5")
coche2=vehiculos("seat", "leon")
coche3=vehiculos("renault", "megane")

coches=[coche1,coche2,coche3]

fichero=open("loscoches", "wb")    #wb es escritura de bits
pickle.dump(coches,fichero)
fichero.close()
del (fichero)

ficheroApertura=open("loscoches", "rb")
misCOches=pickle.load(ficheroApertura)
ficheroApertura.close()
for c in misCOches:
    print(c.estado)