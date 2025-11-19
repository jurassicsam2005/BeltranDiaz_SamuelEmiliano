# Pide al usuario ingresar 10 productos y alamcenalos en una lista. Luego muesytra la lista ordenada alfabeticamente.
productos = []
for _ in range(10):
    producto = input("Ingrese el nombre de un producto: ")
    productos.append(producto) 
productos.sort()
print("Lista de productos ordenada alfabeticamente:")
for producto in productos:
    print(producto)