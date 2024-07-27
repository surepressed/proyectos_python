ingresar_texto = input("Ingresa un texto: ")
letras = []
ingresar_texto = ingresar_texto.lower()

#tomas es el gato mas negro de todas las galaxias

letras.append(input("Ahora ingresa la letra1: ").lower())
letras.append(input("Ahora ingresa la letra2: ").lower())
letras.append(input("Ahora ingresa la letra3: ").lower())

cantidad_letras1 = ingresar_texto.count(letras[0])
cantidad_letras3 = ingresar_texto.count(letras[1])
cantidad_letras2 = ingresar_texto.count(letras[2])

print("\n")
print("NUMERO DE LETRAS REPETIDAS: ")

print(f"La letra '{letras[0]}' se repite {cantidad_letras1} veces")
print(f"La letra '{letras[1]}' se repite {cantidad_letras2} veces")
print(f"La letra '{letras[2]}' se repite {cantidad_letras3} veces")

print("\n")
print("NUMERO DE PALABRAS EN TOTAL: ")

cantidad_palabras = ingresar_texto.split()
print(len(cantidad_palabras))

print("Primera letra: ")
primera_texto = ingresar_texto[0]
print(primera_texto)

print("Ultima letra: ")
ultima_texto = ingresar_texto[-1]
print(ultima_texto)

print("\n")
print("ASI QUEDARIA EL TEXTO INVERTIDO:")
invertir_texto = ingresar_texto[::-1]
print(invertir_texto)

print("\n")

print("BUSCAR SI ESTA LA PALABRA:")

palabra = input("Dime una palabra que quieras comprobar: ")
buscar_palabra = palabra in ingresar_texto
print(buscar_palabra)


