#Haz un programa que pida un número, y calcule la suma de todos los números, desde el 1 hasta ese número. Por ejemplo, si ingresas 5, deberás sumar 1 + 2 + 3 + 4 +5.

numero = int(input("Ingrese un numero"))

suma = 0

for i in range(1, numero + 1):
    suma = suma + i

print(f"La suma de los numeros es {suma}")