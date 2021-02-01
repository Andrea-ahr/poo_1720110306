class Estudiante():

   
   matricula = None
   carrera = None
   turno = None
   escuela = None
   taller = None
   altura = None
   peso = None 
   reputacion = None
   autoestima = None
   curiosidad = None

   def __init__(self):
    print("clase Estudiante")

   

   def leer(self):
        print("Metodo leer")

   def escribir(self):
        print("Metodo escribir")

   def participar(self):
        print("Metodo participar")

   def hacer_practicas(self):
        print("Metodo hacer practicas"
    
   def adelantar_materias(self):
         print("Metodo hacer practicas")

# Creacion de un objeto basado en una clase
Andrea = Estudiante()

Andrea.matricula = 1720110306
Andrea.carrera = "TIC´S"
Andrea.turno = "Matutino"
Andrea.escuela = "UTEC"
Andrea.taller = "Danza"
Andrea.altura = 1.53
Andrea.peso = 53
Andrea.reputacion = "Buena"
Andrea.autoestima = "Si"
Andrea.curiosidad = "Programacion"

print(Andrea.matricula)
print(Andrea.carrera)
print(Andrea.turno)
print(Andrea.escuela)
print(Andrea.taller)
print(Andrea.altura)
print(Andrea.peso)
print(Andrea.reputacion)
print(Andrea.autoestima)
print(Andrea.curiosidad)

Andrea.leer()
Andrea.escribir()
Andrea.participar()
Andrea.hacer_practicas()
Andrea.adelantar_materias ()