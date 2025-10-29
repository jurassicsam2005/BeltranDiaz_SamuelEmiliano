#Haz un programa en Python que calcule el perimetro de una circunferencia con base en su radio
import math

#pedir el radio al usuario
radio = float(input("Ingresa el radio de la circunferencia: "))

#Calcular el perimetro 
perimetro = 2 * math.pi * radio

#Mostrar el perimetro con dos decimales
print("El perimetro de la circunferencia es: {:.2f}" .format(perimetro))
