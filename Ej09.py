num1 = int(input("Ingrese un número: "))
num2 = int(input("Ingrese otro número: "))
oper = input("Ingrese una operación: +, -, *, /, %, **: ")
match oper:
    case "+":
        resultado = num1 + num2
    case "-":
        resultado = num1 - num2
    case "*":
        resultado = num1 * num2
    case "/":
        if num2 != 0: resultado = num1 / num2
        else: resultado = None
    case "%":
        if num2 != 0: resultado = num1 % num2
        else: resultado = None
    case "**":
        resultado = num1 ** num2
    case _:
        resultado = None
if resultado is not None:
    print(f"Resultado: {resultado}")
else:
    if num2 == 0:
        print("No se puede dividir entre 0")
    else:
        print("operacion no reconocida")