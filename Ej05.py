import random
dif = int(input("Ingrese el nivel de dificultad (entero): "))
numC = random.randint(1, dif)
numP = int(input(f"Ahora ingrese un numero entre 1 y {dif}: "))
ganador = "Computadora"
if (numC == numP):
    ganador = "Jugador"
print(f"\nNivel de dificultad: {dif}")
print(f"Numero generado por la computadora: {numC}")
print(f"Numero ingresado por el jugador: {numP}")
print(f"El ganador del juego fue: {ganador}")