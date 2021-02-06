class Futbolista() 

    #Propiedades o caracteristicas

    genero = None
    equipo = None
    posicion = None
    altura = None
    }uniforme = None
    peso = None
    condicion = None
    estrategias = None
    nacionalidad = None
    descendencia = None

    def __init__(self):
        print("Clase Estudiante")

    #Metodos

    def correr(self):
        print("Metodo correr")

    def hablar(self):
        print("Metodo hablar")

    def jugar(self):
        primt("Metodo jugar")

    def comer(self):
        print("Metodo comer")

    def practicar(self):
        print("Metodo practicar")

#Creacion de un ibjeto basado en las propiedades
messi = Futbolista()

#Asignaion de valores a las propiedades
messi.genero = "Masculino"
messi.equipo = "Barcelona"
messi.posicion = "Delantero"
messi.altura = "1.7 m"
messi.uniforme = "Rojo con azul"
messi.peso = "72 kg"
messi.condicion = "Buena"
messi.estrategia = "Buena"
messi.nacionalidad = "Argentina"
messi.descendencia = "Si"

print(messi.genero)
print(messi.equipo)
print(messi.posicion)
print(messi.altura)
print(messi.uniforme)
print(messi.peso)
print(messi.condicion)
print(messi.estrategia)
print(messi.nacinalidad)
print(messi.descendencia)

messi.correr()
messi.hablar()
messi.jugar()
messi.comer()
messi.practicar() 