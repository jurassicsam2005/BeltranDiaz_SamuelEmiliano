# Pide una palabra y reemplaza todas las vocales por el simbolo *.
palabra = input("Ingrese una palabra: ")
resultado = ""
for caracter in palabra:
    if caracter.lower() in "aeiou":
        resultado += "*"
    else:
        resultado += caracter
print("Palabra modificada:", resultado)