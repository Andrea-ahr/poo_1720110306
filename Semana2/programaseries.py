class Series():

    # Propiedades o caracteristicas

    genero = None
    capitulos = None
    temporada = None
    idiomas = None
    subtitulos = None
    resumen = None
    plataforma = None
    historia = None
    elenco = None
    produccion = None
    
    def __init__(self):
        print("Clase Series")

    # Metodos

    def entretener(self):
        print("Metodo entretener")

    def reflexionar(self):
        print("Metodo reflexionar")

    def empezar(self):
        print("Metodo empezar")

    def terminar(self):
        print("Metodo terminar")

    def adelantar(self):
        print("Metodo adelantar")
    
#Creacion de un objeto basado en una clase
Anne = Series()

#Asignacion de valores a las propiedades
Anne.genero = "Amor"
Anne.capitulos = 10
Anne.temporadas = 3
Anne.idioma = "español"
Anne.subtitulos = "ingles"
Anne.resumen = "si"
Anne.plataforma = "netflix"
Anne.historia = "española"
Anne.elenco = "completo"
Anne.produccion = "buena"

print(Anne.genero)
print(Anne.capitulos)
print(Anne.temporadas)
print(Anne.idioma)
print(Anne.subtitulos)
print(Anne.resumen)
print(Anne.plataforma)
print(Anne.historia)
print(Anne.elenco)
print(Anne.produccion)

Anne.entretener()
Anne.reflexionar()
Anne.empezar()
Anne.terminar()
Ann.adelantar()