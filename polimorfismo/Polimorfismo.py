class Vehiculo:
    def arrancar(self):
        print("El vehículo está arrancando...")

class Coche(Vehiculo):
    def arrancar(self):
        print("El coche está arrancando con llave...")

class Moto(Vehiculo):
    def arrancar(self):
        print("La moto arranca con botón...")

# Función fuera de las clases
def iniciar_vehiculo(vehiculo):
    vehiculo.arrancar()

# Probar el polimorfismo
auto = Coche()
moto = Moto()

iniciar_vehiculo(auto)
iniciar_vehiculo(moto)
