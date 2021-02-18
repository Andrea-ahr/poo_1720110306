import math

print("Ingresa los valores para la coordenada 1:")
x1 = int(input ("Ingrese el valor de y1:"))
y1 = int(input("Ingrese el valor de x2:"))
print("Ingresa los valores para la coordenada 2:")
x2 = int(input("Ingrese el valor de x2:"))
y2 = int(input("Ingrese el valor de x2:"))

distancia = math.sqrt((x2-x1)*2+(y2-y1)*2)
print("La distancia es:", + distancia)  