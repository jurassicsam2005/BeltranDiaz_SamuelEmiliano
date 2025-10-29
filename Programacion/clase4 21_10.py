#Programa que pida un numero entereo positivo y muestre su raiz cuadrada, raiz cubica 
#potencial al cuadrado y potencia al cubo 

import math 

numero = int(input("Ingresa un numero entero positivo: "))

raizCuadrada = math.sqrt(numero)
raizCubica = numero ** (1/3)
potenciaCuadrada = pow(numero, 2)
potenciaCubica = pow(numero, 3) 

print(f"La raiz cuadrada de {numero} es: {raizCuadrada}")
print(f"La raiz cubica de {numero} es: {raizCubica}")
print(f"La potencia al cuadrado de {numero} es: {potenciaCuadrada}")
print(f"La potencia al cubo de {numero} es: {potenciaCubica}")