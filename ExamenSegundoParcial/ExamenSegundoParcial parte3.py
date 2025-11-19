# Haz un programa que pida un numero entero N, calcula la suma de todos los numeros del 1 al N.
n = int(input("Ingrese un numero entero N: "))
suma = 0
for i in range(1, n + 1):
    suma += i

print("La suma de los numeros del 1 al", n, "es", suma)