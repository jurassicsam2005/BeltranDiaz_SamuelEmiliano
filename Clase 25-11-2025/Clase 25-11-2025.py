# # Función para mostrar las opciones del menu
# def mostrar_menu():
#     print("Sistema de Gestión de Estudiantes")
#     print("1. Agregar estudiante")
#     print("2. Mostrar lista completa de estudiantes")
#     print("3. Buscar estudiante por nombre")
#     print("4. Eliminar estudiante")
#     print("5. Salir")
    
# # Función para agregar un estudiante
# def agregar_estudiante(lista_estudiantes):
#     nombre = input("Ingrese el nombre del estudiante: ")
#     apellido = input("Ingrese el apellido del estudiante: ")
#     promedio = float(input("Ingrese el promedio del estudiante: "))
    
#     lista_estudiantes.append({"nombre": nombre, "apellido": apellido, "promedio": promedio})
    
#     print(f"Estudiante {nombre} {apellido} agregado exitosamente.")

# # Función para mostrar lista de estudiantes
# def mostrar_estudiantes(lista_estudiantes):
#     if not lista_estudiantes:
#         print("No hay estudiantes en la lista")
#         return
#     print("Lista de estudiantes")
#     for estudiante in lista_estudiantes:
#         print(f"{estudiante['nombre']} {estudiante['apellido']} -  Promedio: {estudiante['promedio']}")
        
# # Función para buscar estudiante por nombre
# def buscar_estudiante(lista_estudiantes):
#     nombre_buscar = input("Ingrese el nombre del estudiante que desea buscar: ")
#     for estudiante in lista_estudiantes:
#         if estudiante['nombre'].lower() == nombre_buscar.lower():
#             print(f"Estudiante encontrado: {estudiante['nombre']} {estudiante['apellido']} - Promedio: {estudiante['promedio']}")
#             return
#     print("Estudiante no encontrado.")
    
# # Función para eliminar estudiante
# def eliminar_estudiante(lista_estudiantes):
#     nombre_eliminar = input("Ingrese el nombre del estudiante que desea eliminar: ")
#     for estudiante in lista_estudiantes:
#         if estudiante['nombre'].lower() == nombre_eliminar.lower():
#             lista_estudiantes.remove(estudiante)
#             print(f"Estudiante {estudiante['nombre']} {estudiante['apellido']} dado de baja exitosamente.")
#             return
#     print("Estudiante no encontrado.")

# Funcion para buscar estudinate por medio del apellido
def buscar_estudiante_por_apellido(lista_estudiantes):
    apellido = input("Ingrese el apellido del estudiante que desea buscar: ")
    encontrados = [estudiante for estudiante in lista_estudiantes if estudiante['apellido'].lower() == apellido.lower()]
    if encontrados:
        print("Estudiantes encontrados:")
        for estudiante in encontrados:
            print(f"{estudiante['nombre']} {estudiante['apellido']} - Promedio: {estudiante['promedio']}")
        else:
            print("No se encontraron estudiantes con ese apellido. ")

# Funcion para calcular el promdeio del grupo
def calcular_promedio_grupo(lista_estudiantes):
    if not lista_estudiantes:
        print("No hay estudiantes en la lista para calcular el promedio: ")
        return
    suma_promedios = sum(estudiante['promedio'] for estudiante in lista_estudiantes)
    promedio = suma_promedios / len(lista_estudiantes)
    print(f"El promedio del grupo es: {promedio:.2f}")

# Funcion para ordenar estudiantes por promedio (De la calificacion mas alta a la mas baja)
def ordenar_estudiantes_por_promedio(lista_estudiantes):
    lista_ordenada = sorted(lista_estudiantes, key=lambda x: x['promedio'], reverse=True)
    print("Estudiantes ordenados por promedio (de mayor a nenor): ")
    for estudiante in lista_ordenada:
        print(f"{estudiante['nombre']} {estudiante['apellido']} - Promedio: {estudiante['promedio']}")