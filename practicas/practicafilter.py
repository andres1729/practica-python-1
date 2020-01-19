'''def numero_par(num):
    if num % 2==0:
        return True

numeros=[43,5,65,33,32,54,65]
print(list(filter(numero_par, numeros))) '''

#podemos simplificar el codigo con el uso de las funciones lambda

# numeros=[43,5,65,33,32,54,65]
#print(list(filter(lambda numero_par: numero_par%2==0, numeros)))
#
class Empleado:
    def ___init__(self, nombre, cargo, salario):
        self.nombre=nombre
        self.cargo=cargo
        self.salario=salario
    def __str__(self):
        return "{} que trabaja como {} tiene salario de {} $".format(self.nombre, self.cargo, self.salario)

listaEmpleados=[
Empleado("Lulu", "Director", 43253),
Empleado("Lily", "Presidente", 4453253),
Empleado("Lola", "Administrativo", 53253),
Empleado("Bert", "Obrero", 253),

]

salarios_altos=filter(lambda empleado: empleado.salario > 4000, listaEmpleados)
for empleado_salario in salarios_altos:
    print(empleado_salario)