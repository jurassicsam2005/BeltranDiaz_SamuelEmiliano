#Haz un programa en Python que pida el radio y la altura de un ciclindro y muestre su volumen
import math
radio = float(input("Ingrese el radio del cilindro: "))
altura = float(input("Ingrese la altura del cilindro: "))
volumen = math.pi * radio**2 * altura
print("El volumen del cilindro es:", volumen)