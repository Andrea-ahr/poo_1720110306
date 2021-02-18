'''
Andrea Hernandez Riveros
TIC 21
17 - feb - 2021
Pedir numero de calculos que se desea calcular y posteriormete realizar el calculo de los segundos
'''

class LeerDatos():

    dias = 0

    def __init__(self):
        pass

    def LeerDias(self):
        self.dias = input("Escribe los dias")

objeto = LeerDatos()
print(type(objeto.dias))
print(type(objeto.dias))
print(type(objeto))

segundo = 1
minuto = 60
hora = 3600
dia = 86400
print("Dame los dias")
dias = int(input(""))
calculos = dia * dias
print("Numero de segundos es:", + calculos)
