# Haz un programa que pida el nombre de un contacto y su teléfono, y los agregue a un diccionario.
contactos = {}
nombre = input("Ingrese el nombre del contacto: ")
telefono = input("Ingrese el telefono del contacto: ")
contactos[nombre] = telefono
print("Contacto agregado:", contactos)