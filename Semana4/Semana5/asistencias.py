'''
Andrea Hernandez Riveros
TIC 21
31 - marzo - 2021
Mostrar si los alumnos tienen derecho a realizar el examen ordinario correspondiente segun las calificaciones y asistencias
'''

class Persona():

    materia = None
    numero_alumnos = None
    nombre_alumno = None
    numero_clases = None
    numero_faltas = None
    retardos = None
    porcentaje_asistencias = None
    resultdo = None

    def_init_(self):
        pass

    def imprimirDatos(self):

        print("Materia", self.materia)
        print("Numero de alumnos", self.numero_alumnos)
        print("Nombre de alumno", self.nombre_alumno)
        print("Numero de clases", self.numero_clases)
        print("Numero de faltas", self.numero_faltas)
        print("Retardos", self.retardos)
        print("Porcentaje de asistencias", self.procentaje_asistencias)
        print("Resultado", self.resultado)

    def bucleWhile(self):

        repetir = "si"
        while repetir = "si":
            print("Otra evaluacion", self.nombre)
            repetir = input("Otra evaluacion (s/n)")

    def bucleFor(self):

        for i in range(2):
            print("Nombre de alumno{}".format(self.nombre))

    