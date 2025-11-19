# Haz un programa que pida una frase y cuenta cuantas letras tiene la frase, sin contar espacios.
frase = input("Ingrese una frase: ")
contador_letras = 0
for caracter in frase:
    if caracter != " ":
        contador_letras += 1
print("La cantidad de letras en la frase es:", contador_letras)