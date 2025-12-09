# En Python existen los siguientes modos de lectura y escritura de archivos:
# 'r' : Modo de lectura (read) -> Abre un archivo para leerlo. El archivo debe existir, sino existe el programa nos marcara error.
# 'w' : Modo de escritura (write) -> Abre un archivo para escribir en el. Si el archivo ya existe se sobreescribe. Si no existe se crea uno nuevo.
# 'a' : Modo de anexado (append) -> Abre un archivo para agregar contenido al final del archivo. Si el archivo no existe, se crea uno nuevo.
# 'r+' : Modo de lectura y escritura -> Abre un archivo para leer y escribir, si el archivo no existe se marcara error 
# 'w+' : Modo de escritura y lectura -> Abre un archivo para escribir y leer, si el archivo no existe, se crea uno nuevo. sobreescribe el archivo si ya existe.
# 'a+' : Modo de anexado y lectura -> Abre un archivo para agregar contenido al final y leerlo, si el archivo no existe, se crea uno nuevo.

#Apertura de archivo
# open("ruta/archivo.txt", modo)

# Cerrar el archivo 
# archivo.close()

# Podemos abrir el archivo haciendo uso del 'with' el cual cierra el archivo de manera automatica al finalizar el bloque de codigo 

# with open("ruta/archivo.txt", modo) as archivo:
#     # Operaciones con el archivo

with open("archivo.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)

# with open("archivo.txt", "r") as f:
#     contenido = f.read() # Leer todo el contenido del archivo, y lo alamcena en la variable contenido
#     print(contenido) 

# with open("archivo.txt", "w") as f:
#     for linea in f: # Leer el archivo linea por linea 
#         print(linea.strip()) # Imprimir cada linea sin espacios adicionales

# with open("archivo2.txt", "a") as f:
#     f.write("Esta es una nueva linea escrita en el archivo.\n")
#     f.write("Otra linea añadida al archivo.\n")

# with open("archivo3.txt", "a") as f:
#     f.write("Esta liena se ha añadido al archivo.\n") 

# with open("archivo.txt", "r+") as f:
#     contenido = f.read()
#     f.write("\nEsta linea se ha añadido al final del archivo usando r+.\n") 

# with open("archivo2.txt", "w+") as f:
#     f.write("Escribiendo en archivo2 usando w+.\n")
#     f.seek(0) # Volver al inicio del archivo para leer lo que se ha escrito
#     contenido = f.read()
#     print(contenido)

# with open("archivo3.txt", "a+") as f:
#     f.write("Añadiendo una linea usando a+.\n")
#     f.seek(0) # Volver al inicio del archivo para leer todo el contenido
#     contenido = f.read()
#     print(contenido) 