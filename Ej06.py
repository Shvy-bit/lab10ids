num1 = int(input("Ingrese un número (entero): "))
num2 = int(input("Ingrese otro número (entero): "))
num3 = int(input("Ingrese otro número (entero): "))
out = num1 * num3
mayor = num1
if num2 > mayor: mayor = num2
if num3 > mayor: mayor = num3
if mayor == num1:
    out = num1 + num2 + num3
if mayor == num2:
    out = num2 - num1
print(f"El resultado es: {out}")