class Calculadora():

    #Propiedades o caracteristicas

    tipo = None
    tamaño = None
    accesorios = None
    materia = None
    bateria = None
    precio = None
    color = None
    funciones = None
    diseño = None
    teclado = None

    def __init__(self):
        print("Clase Calculadora")

    #Metodos

    def sumar(self):
        print("Metodo sumar")

    def restar(self):
        print("Metodo restar")

    def dividir(self):
        print("Metodo dividir")

    def multiplicar(self):
        print("Metodo multiplicar")

    def sacar_raiz(self):
        print("Metodo sacar raiz")

#Creacion de un objeto basado en una clase
Cientifica = Calculadora()

#Asignacion de valores a las propiedades

cientifica.tipo = "cientifica"
cientifica.tamano = "mediano"
cientifica.accesorios = "si"
cientifica.material = "plastico"
cientifica.bateria = 2
cientifica.precio = 250
cientifica.color = "gris"
cientifica.funciones = "matematicas"
cientifica.diseño = "rectangular"
cientifica.teclado = "comodo"

print(cientifica.tipo)
print(cientifica.tamano)
print(cientifica.accesorios)
print(cientifica.material)
print(cientifica.bateria)
print(cientifica.precio)
print(cientifica.color)
print(cientifica.funciones)
print(cientifica.diseño)
print(Icientifica.teclado)

cientifica.sumar()
cientifica.restar()
cientifica.dividir()
cientifica.multiplicar()
cientifica.sacar_raiz()