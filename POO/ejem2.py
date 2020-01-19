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


class furgoneta(vehiculos):
    def carga(self, cargar):
        self.cargado=cargar
        if(self.cargado):
            return "La furgoneta esta cargada"
        else:
            return "La furgoneta no esta cargada"


class moto(vehiculos):           #clase moto que hereda de la clase vehiculo
    hcaballito=""
    def caballito(self):
        self.hcaballito="Voy haciendo caballito"

    def estado(self):
        print("Marca", self.marca, "\nmodelo:", self.modelo, "\En marcha:", self.enmarcha, "\nAcelerando:",
              self.acelera, "\nFrenando:", self.frena, "\n", self.hcaballito)


class velectricos():
    def __init__(self):
        self.autonomia=100

    def cargarenergia(self):
        self.cargando=True


mimoto=moto("Honda", "CBR")
mimoto.caballito()
mimoto.estado()

mifurgoneta=furgoneta("Renault", "Kangoo")
mifurgoneta.arrancar()
mifurgoneta.estado()
print(mifurgoneta.carga(True))


class bicicletaelectrica(velectricos,vehiculos):          #doble herencia
    pass

mibici=bicicletaelectrica()
