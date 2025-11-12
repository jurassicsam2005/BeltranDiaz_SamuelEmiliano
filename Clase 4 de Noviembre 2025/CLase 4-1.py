# nombre = "Mario Alonso Segovia Gutierrez"
# cadena2 = "hola a todos mi nombre es mario alonso segovia gutierrez"
# cadena3 = "          hola mundo          "
# cadena4= "Esto es una cadena "
# cadena5 = "Esto es otra cadena"

# print(len(nombre)) # Imprime la longitud de la cadena

# print(nombre.upper()) # Convierte la cadena a mayusculas

# print(nombre.lower()) # Convierte la vadena a minusculas 

# print(cadena2.capitalize()) # Convierte el primer caracter en mayuscula y el resto en minusculas

# print(cadena2.title()) # Convierte la primer letra de cada palabra en mayuscula

# print(cadena3)
# print(cadena3.strip()) # Elimina los espacios en blanco al inicio y al final de la cadena

# cadenaNueva = cadena4 + cadena5
# print(cadenaNueva) # Concateracion de cadenas 

# cadenaMultiplicada = cadena4 * 5
# print(cadenaMultiplicada) # Multipliccion de cadenas

# print(cadena4.replace("a", "s")) # Reemplaza todas la apariciones de "a" por "s"

# cadena6 = "Hola, ¿como estas? ¿Estas buen?"
# indice = cadena6.find("¿") #Busca la posicion de la primera aparacion de "¿"
# print(indice) #Imprime la posicion de la ultima aparicion de "¿"

# indiceUltimo = cadena6.find("¿") # Busca la posocion de la ultima aparicion de "¿"
# print(indiceUltimo) # Imprime la posicion de la ultima aparicion de "¿"

# cadena7 = "anira lava la tina"
# conteo = cadena7.count("a") # Cuenta cuantas veces aparece "a" en la cadena
# print(conteo) # Imprime el conteo de "a"

# print(cadena7.startswith("anita")) # Verifica se la cadena termina con "anita"
# print(cadena7.endswith("tina")) # Verifica se la cadena termina con "tina"

# #Sintaxis de Slicing cadena [inicio:fin:paso] 

# cadena8 = "Hola a todos"
# print(cadena8[0:4]) # Imprime "Hola"
# print(cadena8[:4])  # Imprime "Hola"
# print(cadena8[4:9]) #Imprime "a to"
# print(cadena8[5:])# Imprime "a todos"
# print(cadena8[-2:]) # Imprime "os"
# print(cadena8[::2]) # Imprime "Hl atds"
# print(cadena8[::-1]) # Imprime la cadena al reves "sodot a aloH"

# #Ejercicio1: Pide una frase y muestre la misma frase sin espacios al inicio y al final con todas las letras en mayuscula
# frase = input("Escribe una frae: ")
# fraselimpia = frase.strip().lower()
# print(fraselimpia)

#Ejercicio 2: pide una palabra y comprueba si es un palindromo
palabra = input("Escribe una palabra: ")
palabra_invertida = palabra[::-1]
if palabra.lower() == palabra_invertida.lower():
    print("La palabra es un palindromo")
else:
    print("La palabra no es un palindromo")