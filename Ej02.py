peso = float(input("Ingrese su peso (en Kg): "))
altura = float(input("Ingrese su altura (en mts): "))
IMC = peso / (altura * altura)
if IMC < 25:
    print("Tas bien bru")
else:
    print("Bro tienes sobrepeso :v")