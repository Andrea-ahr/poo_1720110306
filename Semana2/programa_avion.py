class Avion():

    #Propiedades o caracteristicas
    
     cabina = None
     motor = None
     turbina = None
     bodega_equipaje = None 
     tanque_gasolina = None
     forma_aerodinamica = None 
     repelente_lluvia = None
     estabilizador = None
     timon_direccion = None
     generador_oxigeno = None

     def __init__(self):
         print("Clase Avion")

     #Metodos

     def despegar(self):
         print("Metodo despegar")

    def aterrizar(self):
        print("Metodo aterrizar")

    def transportar(self):
        print("Metodo transportar")

    def girar(self):
        print("Metodo girar")

    def encender_luz(self):
        print("Metodo encender luz")

#Creacion de un objeto basado en una clase
militar = Avion()

#Asignacion de valores a las propiedades 
militar.cabina = "Si"
militar.motor = "EJ200"
militar.turbina = "GE9X"
militar.bodega_euipaje = "Medicamento no redeactivo"
militar.tanque_gasolina = "Si"
militar.forma_aerodinamica = "Por las alas"
militar.repelente_lluvia = "Si"
militar.estabilizador = "Si"
militar.timon_direccion = "Si"
militar.generador_oxigeno = "Si" 

print(militar.cabina)
print(militar.motor)
print(militar.turbina)
print(militar.bodega_equipaje)
print(militar.tanque_gasolina)
print(militar.forma_aerodinamica)
print(militar.repelente_lluvia)
print(militar.estabilizador)
print(militar.timon_direcciono)
print(militar.generador_oxigeno)

militar.despegar()
militar.aterrizar()
militar.trasportar()
militar.girar()
militar.encender_luz() 
