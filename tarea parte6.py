# Haz un programa en Python que pida tres números y muestre si se cumple la expresión A < B < C (solo mostrando el resultado lógico)

#Pedir los numeros al usuario
A = float(input("Ingresa el valor de A: "))
B = float(input("Ingresa el valor de B: "))
C = float(input("Ingresa el valor de C: "))

#Evaluar la expresion A < B < C
resultado = A < B < C

#Mostar el resultado logico 
#True si se cumple la expresion, False si no se cumple
print("El resultado de la expresion A < B < C es: {}".format(resultado))
