# Pide una frase y cuenta cuántas vocales usa (a, e, i, o, u).

print("Ingrese una frase. El programa contará cuántas vocales (a, e, i, o, u) contiene.")

# Usamos un while para pedir la frase hasta que no sea vacía
while True:
	frase = input("Frase: ").strip()
	if frase == "":
		print("Frase vacía. Intente de nuevo.")
		continue
	break

# Inicializar contadores para cada vocal usando un diccionario
vocales = { 'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0 }
total = 0

# Recorrer cada carácter de la frase y verificar si es una vocal
for caracter in frase:
	letra = caracter.lower()
	# usar 'in' para comprobar pertenencia en el diccionario de vocales
	if letra in vocales:
		vocales[letra] = vocales[letra] + 1
		total = total + 1

print()  # línea en blanco antes del resumen
print(f"Total de vocales: {total}")
for v in vocales:
	print(f"{v}: {vocales[v]}")

