# Funciones de Pyhton 

# Definicion 
def saludar():
    print("Hola, bienvenidos a la clase de Python")

#Llamada a la funcion 
saludar()

saludar()

saludar()

# Funcion con parametros 
def saludar_persona(nombre, apellido, edad):
    print(f"Hola {nombre} {apellido}, tienes {edad} años.")

#Llamada a la funcion con argumentos
saludar_persona("Mario", "Segovia", 29)
saludar_persona("Jorge", "Ramirez", 39)
saludar_persona("Jorge", "Zuñiga", 29)

# #Funcion con valor de retorno
# def sumar(a, b):
#     return a + b
# resultado = sumar(5)