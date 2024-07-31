from random import *

print("BIENVENIDO AL JUEGO DE ADIVINAR EL NUMERO!!!")
nombre = input("Dime tu nombre: ").lower()
intentos = 0
pregunta = 0
numero = randint(1,100)

print(f"Bueno {nombre} he pensado un numero entre "
      f"el 1 y el 100, y tienes sólo 8 intentos para"
      f" adivinar cuál crees que es el número")

while intentos < 8:
      pregunta = int(input("Ingresa un número: "))
      intentos += 1

      if pregunta not in range(1,100):
            print("Tu numero no está en el rango establecido, sigue intentando")

      elif pregunta < numero:
            print("Te has quedado corto, sigue intentado!")
      elif pregunta > numero:
            print("Te pasaste de la raya, sigue intentando!")
      else:
            print(f"Adivinaste el número Felicidades {nombre}!! te tomó {intentos} intentos.")
            break

if pregunta != numero:
      print("Lo siento te has quedado con 0 intentos")
