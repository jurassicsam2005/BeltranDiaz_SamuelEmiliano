# Pide una cantidad de productos y su precio uno por uno, luego muestra el total con IVA del 16%.

# Pedir cantidad de productos
cantidad = int(input("¿Cuántos productos vas a registrar?: "))

# Variables para almacenar subtotal
subtotal = 0

# Ciclo para pedir precios
for i in range(cantidad):
    precio = float(input(f"Ingrese el precio del producto {i + 1}: $"))
    if precio > 0:
        subtotal = subtotal + precio
    
# Calcular IVA y total
iva = subtotal * 0.16
total = subtotal + iva

# Mostrar resultados
print(f"\nSubtotal: ${subtotal}")
print(f"IVA (16%): ${iva}")
print(f"Total: ${total}")
