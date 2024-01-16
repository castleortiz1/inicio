# Importar la librería random
import random

# Definir una lista de palabras
palabras = ["perro", "gato", "casa", "árbol", "flor"]

# Elegir una palabra al azar
palabra_aleatoria = random.choice(palabras)

# Inicializar el número de intentos
intentos = 0

# Bucle del juego
while True:
    # Pedir al usuario que introduzca una palabra
    palabra_usuario = input("Introduce una palabra: ")

    # Incrementar el número de intentos
    intentos += 1

    # Comprobar si la palabra es correcta
    if palabra_usuario == palabra_aleatoria:
        print("¡Felicidades! Has adivinado la palabra en", intentos, "intentos.")
        break
    else:
        print("Lo siento, la palabra no es correcta. Inténtalo de nuevo.")

# Mostrar la palabra correcta
print("La palabra correcta era:", palabra_aleatoria)
