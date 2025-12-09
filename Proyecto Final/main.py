from functions import *

# Función principal del sistema
def _main_():
    lista_productos = []
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            agregar_producto(lista_productos)
        elif opcion == '2':
            mostrar_productos(lista_productos)
        elif opcion == '3':
            buscar_producto(lista_productos)
        elif opcion == '4':
            buscar_producto_id(lista_productos)
        elif opcion == '5':
            eliminar_producto(lista_productos)
        elif opcion == '6':
            editar_producto(lista_productos)
        elif opcion == '7':
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

_main_()