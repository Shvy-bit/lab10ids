##desigualdad triangular
lado1 = float(input("Ingrese el 1er lado del triángulo "))
lado2 = float(input("Ingrese el 2do lado del triángulo "))
lado3 = float(input("Ingrese el 3er lado del triángulo "))
esTriangulo = True
if lado1 + lado2 < lado3:
    esTriangulo = False
if lado2 + lado3 < lado1:
    esTriangulo = False
if lado1 + lado3 < lado2:
    esTriangulo = False
tipo = ""
if esTriangulo:
    if lado1 == lado2 == lado3:
        tipo = "equilatero"
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        tipo = "isoceles"
    else:
        tipo = "escaleno"
    print(f"El triangulo es {tipo}")
else:
    print("Eso no es un triangulo")