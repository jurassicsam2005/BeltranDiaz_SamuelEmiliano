#Haz un programam en Python que convierta una cantidad de minutos a horas

#Pedir los minutos al usuario
minutos = int(input("Ingresa la cantidad de minutos a convertir: "))

#Convertir minutos a horas
horas = minutos / 60

#Mostrar el resultado con dos decimales
print("La cantidad de minutos en horas es: {:.2f}" .format(horas))