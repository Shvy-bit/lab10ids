figura = input("Ingrese el nombre de una figura (triangulo, cuadrado, rectangulo): ")
ladoP = float(input("Ingrese el largo de un lado: "))
area = None
match figura:
    case "cuadrado":
        area = 4 * ladoP
    case "rectangulo":
        ladoS = float(input("Ingrese el largo del otro lado: "))
        area = 2 * (ladoP + ladoS)
    case "triangulo":
        print("tamos jodidos")
        area = 1
if area is not None:
    print(f"El area de: {figura} es: {area}")
else:
    print("Algo salio mal :v")


#Falta hallar el area del triagnulo y verificar valores, que no sean negativos y que el triangulo exista xdxdxdxd