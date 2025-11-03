# Haz un programa que pida un número y muestre si es divisible entre 2, 3 o ambos.

numero = int(input("Ingrese un numero"))

if (numero % 2 == 0) and (numero % 3 == 0):
    print("Numero es divisible entre 2 y entre 3")
elif numero % 3 == 0:
    print("Numero es divisible entre 3")
elif (numero % 2 != 0) and (numero % 3 != 0):
    print("No es divisible entre 2 y ni entre 3")
elif numero % 2 == 0:
    print("Es divisible entre 2")
