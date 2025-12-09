import json

# Función para mostrar las opciones del menu
def mostrar_menu():
    print("Abarrotes 'Raccon City'")
    print("Sistema de Gestión de Productos")
    print("1. Agregar un producto")
    print("2. Mostrar lista completa de productos")
    print("3. Buscar producto por nombre")
    print("4. Buscar producto por ID")
    print("5. Eliminar producto")
    print("6. Editar producto")
    print("7. Salir")

# Funcion para cargar el archivo json
def cargar_archivo():
    try:
        with open("productos.json", "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except FileNotFoundError:  # Si no aun no existe el archivo, se devuelve una lista vacia
        return []
    except json.JSONDecodeError:    # Si el archivo esta vacio, reiniciamos como lista vacia
        return []

# Función para guardar la lista completa en el archivo json
def guardar_en_archivo(lista):
    with open("productos.json", "w", encoding="utf-8") as archivo:
        json.dump(lista, archivo, ensure_ascii=False, indent=4)

# Función para agregar un producto
def agregar_producto(lista_productos=None):     #Se agrego "lista_productos=None" para que el programa siga trabajndo aunque la lista este vacia y no borre elemntos anteriores cuando se ingrese uno nuevo
    lista = cargar_archivo()  #carga la lista actual 

    #Ciclo while para que no se deje en blanco el nombre
    while True:
        nombre = input("Ingrese el nombre del producto: ")
        if (nombre.strip() == ""):
            print("Necesitas ingresar un nombre. Intente de nuevo.")
        else:
            break

    #Ciclo for para verificar que no se repita el nombre del producto
    for producto in lista:
        if producto['nombre'].lower() == nombre.lower():
            print("Producto ya registrado")
            return
    
    while True:
        id = input("Ingrese el ID del producto: ")
        if (id.strip() == ""):
            print("Necesitas ingresar un id. Intente de nuevo.")
        else:
            break

    #Otro ciclo for para verificar que el ID no este siendo usado tambien xd
    for producto in lista:
        if producto['ID'].lower() == id.lower():
            print("Este ID ya esta en uso.")
            return

    #Ciclo while true para control de errores usando try except, si ingresa un valor que no es numerico en el precio, el try except detecta el error y ahora temuestra un mensaje, con el ciclo while hace que se repita hasta que ingreses un valor numerico 
    while True:
        try:
            precio = float(input("Ingrese el precio del producto: "))
            break 
        except ValueError:
            print("Necesitas ingresar un valor numerico. Intente de nuevo.")
    
    #Lo mismo que el anterior, solo que ahora necesita ser un valor numerico entero
    while True:
        try:
            cantidad = int(input("Ingrese la cantidad disponible del producto: "))
            break
        except ValueError:
            print("Necesitas ingresar un valor numerico entero. Intente de nuevo.")

    
    while True:
        categoria = input("Ingrese la categoria del producto: ")
        if (categoria.strip() == ""):
            print("Necesitas ingresar un id. Intente de nuevo.")
        else:
            break

    #Aqui guardamos en la lista el diccionario definiendo cual es la clave y cual es su valor
    lista.append({"nombre": nombre, "ID": id, "precio": precio, "cantidad": cantidad, "categoria": categoria})
    
    #Aqui se llama a la funcion para que guarde los cambios en el archivo json
    guardar_en_archivo(lista)
    print(f"El producto '{nombre}' con ID:{id} fue agregado exitosamente.")


# Función para mostrar lista de productos
def mostrar_productos(lista_productos=None):
    lista = cargar_archivo()

    #Si aun no hay nada en la lista, solo se mostrara este mensaje y regresara al menu
    if not lista:
        print("No hay productos en la lista")
        return
    
    lista.sort(key=lambda x: x["nombre"].lower()) #Se usa el sort para ordenar alfabeticamente los productos con respecto al nombre del producto
    print("Lista de productos")
    for producto in lista:
        print(f"{producto['nombre']} - ID: {producto['ID']} - Precio: {producto['precio']} - Cantidad disponible: {producto['cantidad']} - Categoria: {producto['categoria']}") 
        
# Función para buscar productos por nombre
def buscar_producto(lista_productos=None):
    lista = cargar_archivo()

    if not lista:
        print("No hay productos en la lista")
        return
    
    while True:
        nombre_buscar = input("Ingrese el nombre del producto que desea buscar: ")
        if (nombre_buscar.strip() == ""):
            print("Necesitas ingresar un nombre. Intente de nuevo.")
        else:
            break

    for producto in lista:
        if producto['nombre'].lower() == nombre_buscar.lower():   #Se usa el for para buscar el nombre, si el nombre es encontrado, se mostrara el preducto
            print(f"Producto encontrado: {producto['nombre']} - ID:{producto['ID']} - Precio: {producto['precio']} - Cantidad disponible:{producto['cantidad']} - Categoria:{producto['categoria']}")
            return
    print("Producto no encontrado.")

# Funcion para buscar productos por medio de su ID
def buscar_producto_id(lista_productos=None):
    lista = cargar_archivo()
    if not lista:
        print("No hay productos en la lista")
        return
    
    while True:
        id_buscar = input("Ingrese el ID del producto que desea buscar: ")
        if (id_buscar.strip() == ""):
            print("Necesitas ingresar un ID. Intente de nuevo.")
        else:
            break

    for producto in lista:
        if producto['ID'].lower() == id_buscar.lower():
            print(f"Producto encontrado: {producto['nombre']} - ID:{producto['ID']} - Precio: {producto['precio']} - Cantidad disponible:{producto['cantidad']} - Categoria:{producto['categoria']}")
            return
    print("Producto no encontrado.")
    
# Función para eliminar productos
def eliminar_producto(lista_productos=None):
    lista = cargar_archivo()

    if not lista:
        print("No hay productos en la lista")
        return
    
    print("Lista de productos disponibles.")
    for producto in lista:
        print(f"-{producto['nombre']}")

    while True:
        nombre_eliminar = input("Ingrese el nombre del producto que desea eliminar: ")
        if (nombre_eliminar.strip() == ""):
            print("Necesitas ingresar un ID. Intente de nuevo.")
        else:
            break
    
    for producto in lista:
        if producto['nombre'].lower() == nombre_eliminar.lower():
            respuesta = input("Seguro que deseas eliminar este elemento? (Y/N): ")
            if (respuesta.lower() == "y"):
                print("Se removera el producto...")
            elif (respuesta.lower() == "n"):
                print("No se elimino el producto. Regresando al menu principal.")
                return
            else:
                print("Respuesta no valida")
                return
            
            lista.remove(producto)    #Aqui se elimina el producto de nuestra lista
            guardar_en_archivo(lista)   #y aqui se guardan los cambios
            print(f"Producto '{producto['nombre']}' con ID:{producto['ID']} Eliminado exitosamente")
            return
    print("preoducto no encontrado.")

# Funcion para editar productos
def editar_producto(lista_productos=None):
    lista = cargar_archivo()

    if not lista:
        print("No hay productos en la lista")
        return
    
    print("Lista de productos disponibles.")
    for producto in lista:
        print(f"-{producto['nombre']}") 

    while True:
        producto_a_editar = input("Ingresa el nombre del producto que deseas editar: ")
        if (producto_a_editar.strip() == ""):
            print("Necesitas ingresar el nombre de un producto. Intente de nuevo.")
        else:
            break

    for producto in lista:
        if producto['nombre'].lower() == producto_a_editar.lower():
            print(f"Producto '{producto['nombre']}' selecionado.")
            print("Seguro que quieres editar este producto? (Y/N)")
            respuesta = input("R= ")
            if (respuesta.lower() == "n"):
                print("Se cancelo la edicion del producto.")
                return
            elif (respuesta.lower() == "y"):
                print("Mostrando datos para editar") 
            else:
                print("Opcion no valida")
                return
            print("-----------------------------")

            #Aqui se imprimen las claves del producto y sus valores
            for clave, valor in producto.items():
                print(f"{clave}: {valor}")

            while True:
                valor_a_editar = input("Que valor deseas editar?: ")
                if (valor_a_editar.strip() == ""):
                    print("Necesitas ingresar el nombre del valor que deseas editar. Intente de nuevo.")
                else:
                    break

            if (valor_a_editar.lower() == "nombre"):
                while True:
                    nuevo_nombre = input("Ingresa el nuevo nombre del producto: ")
                    if (nuevo_nombre.strip() == ""):
                        print("Necesitas ingresar el nuevo nombre del producto. Intente de nuevo.")
                    else:
                        break

                producto["nombre"] = nuevo_nombre
                guardar_en_archivo(lista)
                print("Nombre editado correctamente")

            elif (valor_a_editar.lower() == "id"):
                while True:
                    nuevo_id = input("Ingresa el nuevo ID del producto: ")
                    if (nuevo_id.strip() == ""):
                        print("Necesitas ingresar el nuevo ID del producto. Intente de nuevo.")
                    else:
                        break

                producto["ID"] = nuevo_id
                guardar_en_archivo(lista)
                print("ID editado correctamente")

            elif (valor_a_editar.lower() == "precio"):
                while True:
                    try:
                        nuevo_precio = float(input("Ingrese el precio del producto: "))
                        break 
                    except ValueError:
                        print("Necesitas ingresar un valor numerico. Intente de nuevo.")
                
                producto["precio"] = nuevo_precio
                guardar_en_archivo(lista)
                print("Precio editado correctamente")

            elif (valor_a_editar.lower() == "cantidad"):
                while True:
                    try:
                        nueva_cantidad = int(input("Ingresa la cantidad actual disponible del producto: "))
                        break 
                    except ValueError:
                        print("Necesitas ingresar un valor numerico entero. Intente de nuevo.")
                
                producto["cantidad"] = nueva_cantidad
                guardar_en_archivo(lista)
                print("Cantidad editada correctamente")

            elif (valor_a_editar.lower() == "categoria"):
                while True:
                    nueva_categoria = input("Ingresa la nueva categoria del producto: ")
                    if (nueva_categoria.strip() == ""):
                        print("Necesitas ingresar la nueva categoria. Intente de nuevo.")
                    else:
                        break
                
                producto["categoria"] = nueva_categoria
                guardar_en_archivo(lista)
                print("Categoria editada correctamente")
                
            else:
                print("Valor para editar no disponible.")