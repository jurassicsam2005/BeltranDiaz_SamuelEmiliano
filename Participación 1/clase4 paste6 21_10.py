#Haz un programa que solicite al usuario la base y la altura de un rectangulo y calcula su area y perimetro
base = float(input("Ingresa la base del rectangulo: "))
altura = float(input("Ingresa la altura del rectangulo: "))

area = base * altura
perimetro = 2 * (base + altura) 

print(f"El area del rectangulo es: {area}")
print(f"El perimetro del rectangulo es: {perimetro}")
