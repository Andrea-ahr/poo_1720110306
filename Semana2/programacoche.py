class Coche():

    #Propiedades o caracteristicas

    marca = None
    color = None
    motor = None
    kilometraje = None
    transmision = None
    año = None
    modelo = None
    velocidad = None
    camper = None
    quemacocos = None

    def __init__(self):
        print("Clase Coche")

    #Metodos

    def acelerar(self):
        print("Metodo acelerar")

    def frenar(self):
        print("Metodo frenar")
    
    def transportar(self):
        print("Metodo transportar")

    def girar(self):
        print("Metodo girar")

    def sonar_claxon(self):
        print("Metodo sonar claxon")

#Creacion de un objeto basado en una clase
camioneta = Coche()

#Asignacion de valores a las propiedades
camioneta.marca = "mazda"
camioneta.color = "blanca"
camioneta.motor = "bueno"
camioneta.kilometraje = 15,000
camioneta.transmision = "automatica
camioneta.año = 2019
camioneta.modelo = "reciente"
camioneta.velocidad = "250 k/h"
camioneta.camoer = "no"
camioneta.quemacocos ="si"

print(camioneta.marca)
print(camioneta.color)
print(camioneta.motor0)
print(camioneta.kilometraje)
print(camioneta.año)
print(camioneta.modelo)
print(camioneta.velocidad)
print(camioneta.camper)
print(camioneta.quemacocos)

camioneta.acelerar()
camioneta.frenar()
camioneta.transportar()
camioneta.girar()
camioneta.sonar_claxon()