# Crea un diccionario con clave y valor producto : precio. Luego, pide una lista de productos comprados y muestra el total de la compra. Si el producto no existe, muestra una advertencia.
productos = {"manzana": 0.5, "banana": 0.3, "leche": 1.2, "pan": 1.0}
entrada = input("Ingrese una lista de productos comprados separados por comas: ")
productos_comprados = [producto.strip() for producto in entrada.split(",")]
total = 0
for producto in productos_comprados:
    if producto in productos:
        total += productos[producto]
    else:
        print(f"Advertencia: El producto '{producto}' no existe en el inventario.") 
    
print(f"Total de la compra: ${total:.2f}")