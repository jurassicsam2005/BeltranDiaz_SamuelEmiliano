# Haz un programa que pida una palabra y verifique si inicia con una vocal.
palabra = input("Ingrese una palabra: ")
if palabra[0].lower() in 'aeiou':
    print("La palabra inicia con una vocal.")
else:
    print("La palabra no inicia con una vocal.")