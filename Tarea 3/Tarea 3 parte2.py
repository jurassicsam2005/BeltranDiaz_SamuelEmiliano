#Haz un programa que solicite números al usuario hasta que ingrese un cero. Al final, imprime cuántos números positivos y negativos introdujo.

numero = float(input("Ingrese el un numero"))
positivos = 0
negativos = 0

while numero != 0:
    if numero > 0:
        positivos = positivos + 1
        numero = float(input("Ingrese el un numero"))
    else:
        negativos = negativos + 1
        numero = float(input("Ingrese el un numero"))

print(f"Los positivos son {positivos} y los negativos son {negativos}")

