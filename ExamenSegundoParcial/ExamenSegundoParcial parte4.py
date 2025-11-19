# Haz un programa que pida una palabra, y cuenta cuantas vocales tiene la palabra ingresada.
palabra = input("Ingrese una palabra: ")
contador_vocales = 0
for caracter in palabra:
    if caracter.lower() in "aeiou":
        contador_vocales += 1

print("La cantidad de vocales en la palabra es:", contador_vocales)