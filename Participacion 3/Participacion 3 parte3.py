# Haz un programa que pida "Nombre" y "Calificación". Almacena todos estos datos en un diccionario.
# Posteriormente muestra: Promedio general, cantidad de aprobados y cantidad de reprobados.
# Implementación: solo se usan ciclos (while y for) y la palabra clave 'in' — sin funciones (def).

print("Ingrese nombres y calificaciones. Escriba 'Fin' como nombre para terminar.")

calificaciones = {}

while True:
	nombre = input("Nombre (o 'Fin' para terminar): ").strip()
	if nombre == "Fin":
		break
	if nombre == "":
		print("Nombre vacío. Intente de nuevo.")
		continue

	# Leer la calificación con un bucle hasta que sea un número válido
	while True:
		entrada = input(f"Calificación de {nombre}: ").strip()
		# aceptar coma o punto como separador decimal
		try:
			cal = float(entrada.replace(',', '.'))
		except Exception:
			print("Calificación inválida. Ingrese un número (por ejemplo 7 o 85.5).")
			continue
		if cal < 0:
			print("La calificación no puede ser negativa.")
			continue
		break

	calificaciones[nombre] = cal

print()
if not calificaciones:
	print("No se ingresaron calificaciones.")
else:
	total = 0.0
	cantidad = 0
	aprobados = 0
	reprobados = 0

	# Detectar escala: si alguien ingresó >10, asumimos escala 0-100 y umbral 60,
	# si no, asumimos escala 0-10 y umbral 6. Esto evita pedir al usuario el umbral.
	max_cal = 0.0
	for nombre in calificaciones:
		if calificaciones[nombre] > max_cal:
			max_cal = calificaciones[nombre]

	if max_cal > 10:
		umbral = 60.0
	else:
		umbral = 6.0

	for nombre in calificaciones:
		total += calificaciones[nombre]
		cantidad += 1
		if calificaciones[nombre] >= umbral:
			aprobados += 1
		else:
			reprobados += 1

	promedio = total / cantidad
	print(f"Promedio general: {promedio:.2f}")
	print(f"Cantidad de aprobados (umbral = {umbral}): {aprobados}")
	print(f"Cantidad de reprobados: {reprobados}")


