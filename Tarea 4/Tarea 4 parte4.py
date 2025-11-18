# Haz un programa que pida un texto y una palabra. Si la palabra está en el texto, muestra cuántas veces aparece
texto = input("Ingrese un texto: ")
palabra = input("Ingrese una palabra a buscar: ")
contador = texto.count(palabra)
print(f"La palabra '{palabra}' aparece {contador} vez/veces en el texto.")