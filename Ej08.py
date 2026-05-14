num1 = int(input("Ingrese un número: "))
num2 = int(input("Ingrese otro número: "))
oper = input("Ingrese una operación: +, -, *, /, %, **: ")
resultado = None
if oper == "+":
    resultado = num1 + num2
if oper == "-":
    resultado = num1 - num2
if oper == "*":
    resultado = num1 * num2
if oper == "/":
    if num2 != 0:
        resultado = num1 / num2
    else:
        resultado = None
if oper == "%":
    if num2 != 0:
        resultado = num1 % num2
    else:
        resultado = None
if oper == "**":
    resultado = num1 ** num2
if resultado is not None:
    print(f"Resultado: {resultado}")
else:
    if num2 != 0:
        print("operacion no reconocida")
    else:
        print("No se puede dividir entre 0")