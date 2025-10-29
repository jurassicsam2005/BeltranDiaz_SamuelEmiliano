#Haz un programa que pida al usuario que ingrese un nombre y una edad, verifica si la persona ingresada tiene la edad suficiente para votar (Tomando en cuenta que se puede votar a partir de los 18 años), si puede votar imprime un mensaje indicando que se puede votar, en caso de que no se pueda, imprime un mensaje indicando que no se puede votar y los años que le faltan para llegar poder votar.

nombre = input("Ingrese un nombre")
edad = int(input("Ingresa una edad"))
edadFaltante = 0

if edad >= 18:
    print("Eres mayor de edad puedes votar")
else:
    for i in range(edad, 18):
        edadFaltante += 1

    print(f"No eres mayor de edad, no puedes votar, te faltan {edadFaltante} años")