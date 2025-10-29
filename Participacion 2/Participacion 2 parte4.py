#Haz un programa que pida 5 números (Técnicamente podríamos almacenarlos en un arreglo, pero no hemos llegado ahí, así que NO LO HAGAS ASÍ, debes pedir los números y almacenarlos en variables diferentes), de los 5 números ingresados, muestra cuántos fueron mayores que 10.

numero1 = float(input("Ingrese el primer numero"))
numero2 = float(input("Ingrese el segundo numero"))
numero3 = float(input("Ingrese el tercer numero"))
numero4 = float(input("Ingrese el cuarto numero"))
numero5 = float(input("Ingrese el quinto numero"))

contadorMayor10 = 0
if numero1 > 10:
    contadorMayor10 += 1

if numero2 > 10:
    contadorMayor10 += 1

if numero3 > 10:
    contadorMayor10 += 1

if numero4 > 10:
    contadorMayor10 += 1

if numero5 > 10:
    contadorMayor10 += 1

print(f"La cantidad de numeros mayores a 10 es de {contadorMayor10}")