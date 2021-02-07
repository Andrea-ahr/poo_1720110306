class Classroom():

    #Propiedades o caracteristicas

    materias = None
    codigos = None
    clases_virtuales = None
    calendario = None
    pendientes = None
    carpetas = None
    configuraciones = None
    cuentas_correo = None
    tipo_usuario = None 
    administradores = None

    def __init__(self):
        print("Clase Classroom")

    #Metodos

    def entrar(self):
        print("Metodo entrar")

    def salir(self):
        print("Metodo salir")

    def entregar(self):
        print("Metodo entregar")

    def recibir(self):
        print("Metodo recibir")
        
    def dialogar(self):
        print("Metodo dialogar")

#Creacion de un objeto basado en una clase 
Google = Classroom()

#Asignacion de valores a las propiedades
Google.materias = 8
Google.codigos = "Si"
Google.clases_virtuales = 8
Google.calendario = "Si"
Google.pendientes = "Si"
Google.carpetas = 4
Google.configuraciones = "Personalizar"
Google.cuentas_correo = 1
Google.tipo_usuario = "Estudiante"
Google.administradores = "Docentes"

print(Google.materias)
print(Google.codigos)
print(Google.clases_virtuales)
print(Google.calendario)
print(Google.pendientes)
print(Google.carpetas)
print(Google.configuraciones)
print(Google.cuentas_correo)
print(Google.tipo_usuario)
print(Google.administradores)

Google.entrar()
Google.salir()
Google.entregar()
Google.recibir()
Google.dialogar()