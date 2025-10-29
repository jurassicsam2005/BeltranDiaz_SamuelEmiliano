# Haz un programa en Python que pida tres calificaciones y calcule su promedio con dos decimales 

#Pedir las calificaciones al usuario
calificacion1 = round(float(input("Ingresa la primera calificacion:")),2)
calificacion2 = round(float(input("Ingresa la segunda calificacion:")),2)
calificacion3 = round(float(input("Ingresa la tercera calificacion:")),2)

#Calcular el promedio
promedio = (calificacion1 + calificacion2 + calificacion3) / 3

#Mostrar el promedio con dos decimales
print("El promedio de las calificaciones es: {:.2f}" .format(promedio))