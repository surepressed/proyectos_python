nombre = input("Cuál es tu nombre?: ")
ventas = int(input("Cuánto has vendido?: "))

comision = round(ventas * 13 / 100,2)

print(f"Hola {nombre} has ganado {comision}")


