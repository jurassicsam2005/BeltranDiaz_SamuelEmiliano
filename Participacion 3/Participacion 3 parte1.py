# Pide nombres hasta que el usuario escriba la palabra "Fin". Al final muestra cuantos nombres ingresó, y cuál es el primero y el último.

# Lista para almacenar los nombres ingresados
nombres = []

while True:
	nombre = input("Nombre (escriba 'Fin' para terminar): ").strip()
	# comparar exactamente con 'Fin' según petición
	if nombre == "Fin":
		break
	# ignorar entradas vacías
	if nombre == "":
		print("Nombre vacío. Intente de nuevo.")
		continue
	nombres.append(nombre)

print()  # línea en blanco antes del resumen
if len(nombres) == 0:
	print("No se ingresaron nombres.")
else:
	print(f"Cantidad de nombres ingresados: {len(nombres)}")
	print(f"Primero: {nombres[0]}")
	print(f"Último: {nombres[-1]}")