class Cajero_Automatico():

    #Propiedades o caracteristicas 

    ranura_tarjeta = None
    NIP = None
    teclado = None
    ranuta_dinero = None
    ranura_recibos = None
    pantalla = None
    proctetor_teclado = None
    energia_electrica = None
    operaciones = None
    informacion = None 

    def __init__(self):
        print("Clase Cajero Automatico")

    
    #Metodos

    def retirar(self):
        print("Metodo retirar")

    def depositar(self):
        print("Metodo depositar")

    def transferir(self):
        print("Metodo transferir")

    def prender(self):
        print("Metodo prender")

    def apagar(self):
        print("Metodo apagar")

#Creacion de un objeto basado en una clase
BBVA = Cajero_Automatico()

#Asignacion de valores a las propiedades
BBVA.ranura_tarjeta = "Si"
BBVA.NIP = "Si"
BBVA.teclado = "Digital"
BBVA.ranura_dinero = "Si"
BBVA.ranura_recibos = "Si"
BBVA.pantalla = "Grande"
BBVA.protector_teclado = "No"
BBVA.energia_electrica = "Si"
BBVA.tipo_operacion = 7
BBVA.informacion = "Operaciones"

print(BBVA.ranura_tarjeta)
print(BBVA.NIP)
print(BBVA.teclado)
print(BBVA.ranura_dinero)
print(BBVA.ranura_recibos)
print(BBVA.pantalla)
print(BBVA.protector_teclado)
print(BBVA.energia_electrica)
print(BBVA.tipo_operacion)
print(BBVA.informacion)

BBVA.retirar()
BBVA.depositar()
BBVA.transferir()
BBVA.prender()
BBVA.apagar()