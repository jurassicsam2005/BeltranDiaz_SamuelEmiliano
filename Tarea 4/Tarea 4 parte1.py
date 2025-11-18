# Pide una frase, divídela en palabras y guarda una lista solo las que tengan más de 5 letras. Muestra la lista resultante.
frase = input("Ingrese una frase: ")
palabras = frase.split()
palabras_mas_de_cinco = [palabra for palabra in palabras if len(palabra) > 5] 
print(palabras_mas_de_cinco)