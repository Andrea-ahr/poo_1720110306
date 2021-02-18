'''
Andrea Hernandez Riveros
TIC 21
17 - feb - 2021
Con este programa se podra calcular el promedio basandonos en diferentes temperaturas
''' 

class LeerDatos():

    temperaturas = 0

    def __init__(self):
        pass

    def LeerTemperaturas(self):
        self.temperaturas = input("Escribe las temperaturas") 

objeto = LeerDatos()
print(type(objeto.temperaturas))
print(type(objeto.temperaturas))
print(type(objeto))

print("Dame el numero de temperaturas")
numero = int(input(""))
print("Temperatura 1")
temperatura1 = int(input(""))
print("Temperatura 2")
temperatura2 = int(input(""))
print("Temperatura 3")
temperatura3 = int(input(""))

celcius = temperatura1 + temperatura2 + temperatura3 / 3
farenheit = celcius * 1.8 + 32
promedio = farenheit 
final = promedio / 3  
print("El promedio en farenheit es:", + promedio)

