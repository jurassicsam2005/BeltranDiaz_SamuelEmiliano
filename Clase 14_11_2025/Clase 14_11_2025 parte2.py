# Sistema de Gestion de Estudiantes

#Funcion para mostrar las opciones del menu 
def mostrar_menu():
    print("Sistema de Gestion de Estudiantes")
    print("1. Agregar estudiantes")
    print("2. Mostrar lista completa de estudiantes")
    print("3. Buscar estudiantes por nombre")
    print("4. Eliminar estudiante")
    print("5. Salir")

# Funcion para agregar un estudiate
def agregar_estudiante(lista_estudiantes):
    nombre = input("Ingrese el nombre del estudiante ")
    apellido = input("Ingrese el apellido del estudiante ")
    promedio = float(input("Ingrese el promedio del estudiante: "))

    lista_estudiantes.append({"nombre": nombre, "apellido": apellido, "promedio": promedio})

    print(f"Estudiante {nombre} {apellido} agregado")

    
