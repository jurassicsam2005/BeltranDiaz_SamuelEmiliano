#Haz un programa que pida un número, y muestre si es primo o no.

numero = int(input("Ingrese un numero"))

primo = 0

for i in range(1, numero + 1):
    if numero % i == 0:
        primo = primo + 1

if primo == 2:
    print("El numero es primo")
else:
    print("El numero no es primo")

