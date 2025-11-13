# Programa: Leer 5 nombres y calificaciones, calcular promedio, mayor, menor y mejor alumno.
# Solo se usan ciclos (for / while)

NUM_ALUMNOS = 5

total = 0.0
mejor_nombre = None
mejor_cal = None
menor_cal = None

for i in range(1, NUM_ALUMNOS + 1):
    nombre = input(f"Nombre {i}: ").strip()
    # Validar entrada numérica para la calificación
    while True:
        entrada = input(f"Calificación de {nombre}: ").strip()
        try:
            cal = float(entrada)
            break
        except ValueError:
            print("Entrada no válida. Introduce un número para la calificación.")
    total += cal

    # Inicializar o actualizar mayor y menor usando ciclos (condiciones dentro del for)
    if mejor_cal is None or cal > mejor_cal:
        mejor_cal = cal
        mejor_nombre = nombre
    if menor_cal is None or cal < menor_cal:
        menor_cal = cal

promedio = total / NUM_ALUMNOS

print("\nResultados:")
print(f"Promedio general: {promedio:.2f}")
print(f"Calificación mayor: {mejor_cal:.2f}")
print(f"Calificación menor: {menor_cal:.2f}")
print(f"Mejor alumno: {mejor_nombre} ({mejor_cal:.2f})")