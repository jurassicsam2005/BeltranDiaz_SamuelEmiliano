#Haz un programa en Python que calcule el area de un circulo a partir de su radio

import math

#Pedir el radio al usuario
radio = float(input("Ingresa el radio del circulo: "))

#Calcular el area
area = math.pi * radio ** 2

#Mostrar el area con dos decimales
print("El area del circulo es: {:.2f}" .format(area))
