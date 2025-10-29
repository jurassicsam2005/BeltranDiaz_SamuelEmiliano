# Haz un programa en Python que pida un precio y muestre el total con IVA (16%) 

#Pedir el precio al usuario
precio = float(input("Ingresa el precio del producto: "))

#Calcular el total con IVA
iva = precio *0.16
total = precio + iva

#Mostrar el resultado con dos decimales
print("El total con IVA es: {:.2f}" .format(total))