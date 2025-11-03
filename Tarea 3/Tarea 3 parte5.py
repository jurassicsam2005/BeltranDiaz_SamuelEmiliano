# #Haz un programa que pida una edad, y dependiendo del rango, muestre una categoría:
#      - Menor de 13 años -> "Niño"
#      - 13 a 17 años -> "Adolescente"
#      - 18 a 64 años -> "Adulto"
#      - 65 o más -> "Adulto mayor"

edad = int(input("Ingrese la edad"))

if edad < 13:
    print("Niño")
elif (edad >= 13) and (edad <= 17):
    print("Adolecente")
elif (edad >= 18) and (edad <= 64):
    print("Adulto")
else:
    print("Adulto mayor")