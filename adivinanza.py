# Importamos la biblioteca random para generar números aleatorios
import random

# Función principal del juego de adivinanza
def juego_adivinanza():
    # Genera un número aleatorio entre 1 y 100
    numero_aleatorio = random.randint(1, 100)

    # Iniciamos un bucle infinito que se rompe cuando el usuario adivina el número
    while True:

        # Solicita al usuario que ingrese un número

        numero_usuario = int(input("Adivine el número (1-100): "))

        # Verifica si el número del usuario es igual al número aleatorio

        if numero_usuario == numero_aleatorio:
            print("¡Felicidades! Adivinaste el número")
            break  # Rompe el bucle si el número es correcto
        # Si el número del usuario es menor que el número aleatorio 
        elif numero_usuario < numero_aleatorio:
            print("El número es mayor")  # Informa al usuario que adivine un número mayor
        # Si el número del usuario es mayor que el número aleatorio
        else:
            print("El número es menor")  # Informa al usuario que adivine un número menor

# Llamada a la función para iniciar el juego
juego_adivinanza()
