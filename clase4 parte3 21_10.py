#Haz un programa que pida la usuario dos numeros, y muestre la suma, resta, multiplicacion y division 

num1 = float(input("Ingresa el primer numero: "))
num2 = float(input("Ingres el segundo numero: "))

suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2 
division = num1 / num2

print(f"La suma de {num1} y {num2} es: {suma}")
print(f"La resta de {num1} y {num2} es: {resta}")
print(f"La multiplicacion de {num1} y {num2} es: {multiplicacion}")
print(f"La division de {num1} y {num2} es: {division}") 