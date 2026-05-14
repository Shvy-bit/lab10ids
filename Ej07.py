import random
lv = int(input("Ingrese un nivel entre 1 y 10: "))
numP = int(input(f"Ingrese un número entre 1 y {10 * lv}: "))
numC = random.randint(1, 10 * lv)
ganador = "Computadora"
if (numC % 2 == numP % 2):
    ganador = "Jugador"
print(f"\nNivel: {lv}")
print(f"Numero generado por la computadora: {numC}")
print(f"Numero ingresado por el jugador: {numP}")
print(f"El ganador del juego fue: {ganador}")