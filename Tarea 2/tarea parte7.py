#Haz un programa en Python que pida un numero y muestre si esta entre 10 y 20 (solo mostrando True o False)

#Pedir el numero al usuario
numero = float(input("Ingresa un numero: "))

#Evaluar si el numero esta entre 10 y 20
resultado = 10 < numero < 20

#Mostrar el resultado logico
print("El resultado de la expresion 10 < numero < 20 es: {}".format(resultado))