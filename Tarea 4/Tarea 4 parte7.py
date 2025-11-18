# Haz un programa en Python que pida repetidamente el nombre de una persona y su respuesta ("Si" o "No"). Guarda cada respuesta en un diccionario, donde la clave sea el nombre y el valor la respuesta. El programa debe terminar cuando el usuario escriba "Fin" como nombre. Al finalizar, muestra cuántas personas respondieron "Si", y cuántas respondieron "No".
respuestas = {}
while True:
    nombre = input("Ingrese el nombre de la persona (o 'Fin' para terminar): ")
    if nombre.lower() == "fin":
        break
    respuesta = input("Ingrese la respuesta (Si/No): ")
    if respuesta.lower() in ["si", "no"]:
        respuestas[nombre] = respuesta.capitalize()
    else:
        print("Respuesta inválida. Por favor, ingrese 'Si' o 'No'.")

si_count = sum(1 for r in respuestas.values() if r == "Si")
no_count = sum(1 for r in respuestas.values() if r == "No")

print(f"Personas que respondieron 'Si': {si_count}")
print(f"Personas que respondieron 'No': {no_count}")