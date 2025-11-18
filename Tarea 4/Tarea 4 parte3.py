# Haz un programa que pida al usuario una contraseña. Verifica que: La contraseña tenga al menos 8 caracteres, y que contenga al menos una mayúscula y un número.
contraseña = input("Ingrese una contraseña: ")
tiene_mayuscula = any(c.isupper() for c in contraseña)
tiene_numero = any(c.isdigit() for c in contraseña)
if len(contraseña) >= 8 and tiene_mayuscula and tiene_numero:
    print("Contraseña valida")
else:
    print("Contraseña invalida. Dbe tener al menos 8 caracteres, una mayuscula y un numero.")