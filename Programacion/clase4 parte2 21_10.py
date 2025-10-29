#Haz un programa que pida tres numeros enteros y muestre si se cumple la expresion: El primer numero es mayor que el segundo y el segundo es menor que el tercero: Esto sin ultilizar condiciones, solo operadores logicos 

num1 = int(input("Ingresa el primer numero entero: "))
num2 = int(input("Ingresa el segundo numero entero: "))
num3 = int(input("Ingresa el tercer numero entero: "))

resultado = (num1 > num2) and (num2 < num3)

print(f'¿Se cumple la proposicion? {resultado}') 