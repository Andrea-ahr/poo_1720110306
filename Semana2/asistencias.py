'''
Andrea Hernandez Riveros
TIC 21
31 - marzo - 2021
Mostrar si los alumnos tienen derecho a realizar el examen ordinario correspondiente segun las calificaciones y asistencias
'''

class persona():

    materia = None
    numero_alumnos = None
    nombre_alumno = None
    numero_clases = None
    numero_faltas = None
    retardos = None
    porcentaje_asistencias = None
    resultdo = None

    def __init__(self):
        pass

        def materia(self):
            print("Materia")

        def numero_alumnos(self):
            print("Numero de alumnos")

        def nombre_alumno(self):
            print("Nombre alumno")

        def numero_clases(self):
            print("Numero de clases")

        def numero_faltas(self):
            print("Numero de faltas")

        def retardos(self):
            print("Numero de retardos")

        def porcentaje_asistencias(self):
            print("Porcentaje de asistencias")

        def resultado(self):
            print("Resultado")

def bucleWhile(self):
    repetir = "s"
    while repetir == "s":
        print("Otraevaluacion",self.nombre)
        repetir = input("Otra evaluacion (s/n)")

def buclefor(self):
    for i in range(2):
        print("Numero de alumno{}".format(self.nombre))

alumno = persona()

alumno.materia = "Programacion Orientada a Objetos"
alumno.numero_alumnos = "2"
alumno.nombre_alumno = "Dejah"
alumno.numero_clases = "10"
alumno.numero_faltas = "2"
alumno.numero_retardos = "2"
alumno.porcentaje_asistencias = "80"
alumno.resultado = "No tiene derecho"

print("Materia:",alumno.materia)
print("Numero de alumnos:",alumno.numero_alumnos)
print("Nombre del alumno:",alumno.nombre_alumno)
print("Numero de clases:",alumno.numero_clases)
print("Numero de faltas:",alumno.numero_faltas)
print("Numero de retardos:",alumno.numero_retardos)
print("Porcentaje de asistencias:",alumno.porcentaje_asistencias)
print("Resultado:",alumno.resultado)

print("Otra evaluacion:","s")

alumno.materia = "Base de datos"
alumno.nombre_alumno = "Jhon"
alumno.numero_alumnos = "2"
alumno.numero_clases = "10"
alumno.numero_faltas = "2"
alumno.numero_retardos ="3"
alumno.porcentaje_asistencias = "70"
alumno.resultado = "No tiene derecho"

print("Materia:",alumno.materia)
print("Nombre del alumno:",alumno.nombre_alumno)
print("Numero de alumnos:",alumno.numero_alumnos)
print("Numero de clases:",alumno.numero_clases)
print("Numero de faltas:",alumno.numero_faltas)
print("Numero de retardos:",alumno.numero_retardos)
print("Porcentaje de asistencias:",alumno.porcentaje_asistencias)
print("Resultado:",alumno.resultado)
