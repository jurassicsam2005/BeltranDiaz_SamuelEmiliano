#Metodo de utilidad
lista_frutas = ["manzana, banana, cereza, durazno, naraja"]
print(lista_frutas)

lista_frutas.append("kiwi") # Agrega un elemnetoal final de la lista
print(lista_frutas)

lista_frutas.pop() # Elimina el ultimo elemento de la lista 
print(lista_frutas)

lista_frutas.pop(2) # Elimina el elemento en la posicion 2 (tercer elemento)
print(lista_frutas)

lista_frutas.remove("banana") # Elimina 
print(lista_frutas)

lista_frutas.insert("uva)")
print(lista_frutas)

lista_frutas.clear()# Elimina todos los ntos elementos de la lista
(lista_frutas)

lista_frutas = [] # Reinicamos la lista para los siguientes ejercicios
print(lista_frutas)

lista_frutas = ["manzana, banana, cereza, durazno, naraja"]
lista_frutas.index("cereza") # Devuelve al indice del elemento cereza
print(lista_frutas.index("cereza")) 

lista_frutas.count("banana") # Cuenta cuantas veces aparece "banana" en la lista
print(lista_frutas.count("banana"))

lista_frutas.sort() # Ordena la lista alfabeticamente 
print(lista_frutas)

lista_frutas.reverse() # Invierte el orden de la losta 
print(lista_frutas)

len(lista_frutas) # Devuelve la cantidad de elementos en la lista
print(len(lista_frutas)) 

lista = [5, 2, 9, 1, 5, 6]
print(sum(lista)) # Suma todos los elementos de la lista

#Egercicio 1: Pide 5 numeros, guardalos en una lista y muestre el promedio y el mayor de los numeros.
lista_numeros = []

#Llenar la losta por medio de un for
for i in range(5): 
    numero = float(input("Ingresa un numero: ")) 
    lista_numeros.append(numero) # Agregamos el numero ingresado por consola a la lista

promedio = sum( lista_numeros) / len(lista_numeros) #Calculamos el promedio
num_mayor = max(lista_numeros) #Obtenemos el numero mayor con la funcion max() y lo guardamos en una variable 
print(f"El promedio de los numeros ingresados es: {promedio}. Y el numero mayor es: {num_mayor}. ")

#Ejercicio 2: Pide numeros hasta que el ususario ingrese 0; guardalos en una lista y muestra la lista ordenda ascendentemente
lista_numeros = []
while True:
    numero = float(input("Ingresa un numero(Ingresa 0 para terminar): "))
    if numero == 0:
        break
    lista_numeros. append(numero)

lista_numeros.sort()
print("Lista ordenada:", lista_numeros)