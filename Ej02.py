#coordenadas, froman un triangulo?, es escaleno isoceles o equilatero
import math
x1 = float(input("Ingrese la 1° coordenada del 1° punto "))
y1 = float(input("Ingrese la 2° coordenada del 1° punto "))
x2 = float(input("Ingrese la 1° coordenada del 2° punto "))
y2 = float(input("Ingrese la 2° coordenada del 2° punto "))
x3 = float(input("Ingrese la 1° coordenada del 3° punto "))
y3 = float(input("Ingrese la 2° coordenada del 3° punto "))

esTriangulo = True
if x1 == x2 == x3 or y1 == y2 == y3:
    esTriangulo = False
if esTriangulo:
    lado1 = math.dist((x1, y1), (x2, y2))
    lado2 = math.dist((x1, y1), (x3, y3))
    lado3 = math.dist((x2, y2), (x3, y3))
    if lado1 == lado2 == lado3:
        tipo = "equilatero"
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        tipo = "isoceles"
    else:
        tipo = "escaleno"
    print(f"El triangulo es {tipo}")
else:
    print("Eso no es un triangulo")
