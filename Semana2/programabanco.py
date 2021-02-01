class Banco():

    cajero_automatico = None
    estacionamiento = None
    locacion = None
    aplicacion = None
    compañia = None
    servicios = None
    Financiamiento = None
    comisiones = None
    sucursales = None
    relacion_con_inmuebles = None

    def __init__(self):
        print("clase banco")

    "Metodos"

    def abrir(self):
        print("Metodo abrir")

    def cerrar(self):
        print("Metodo cerrar")

    def atender(self):
        print("Metdodo atender")

    def cobrar(self):
        print("Metodo cobrar")

    def recibir(self):
        print("Metodo recibir")


# creacion de un objeto basado en una clase
santander = Banco()

# asignacion de valores a las propiedades
santander.cajero = "Si"
santander.estacionamiento = "Si"
santander.locacion = "Centro"
santander.aplicacion = "Si"
santander.compania = 2
santander.servicios = "SuperNet"
santander.financiamiento = "Si"
santander.comisiones = 2
santander.sucusucursales = 1, 400

print(santander.cajero_automatico)
print(santander.estacionamiento)
print(santander.locacion)
print(santander.aplicacion)
print(santander.compañia)
print(santander.servicios)
print(santander.financiamiento)
print(santander.comisiones)
print(santander.sucusucursales)

santander.abrir()
santander.cerrar()
santander.atender()
santander.cobrar()
santander.recibir()