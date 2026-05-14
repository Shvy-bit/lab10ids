num1 = int(input("Ingrese un número (entero): "))
num2 = int(input("Ingrese otro número (entero): "))
if num1 < num2:
    print(f"La multiplicación de { num2 } y { num1 } es: { (num2 * num1)}")
    print(f"La división de { num2 } y { num1 } es: { (num2 / num1)}")
    print(f"La división entera de { num2 } y { num1 } es: { (num2 // num1)}")
    print(f"El módulo de { num2 } y { num1 } es: { (num2 % num1)}")
    print(f"La potencia de { num1 } sobre { num2 } es: { (num2 ** num1)}")
else:
    print(f"La suma de { num1 } y { num2 } es: { (num1 + num2)}")
    print(f"La resta de { num1 } y { num2 } es: { (num1 - num2)}")