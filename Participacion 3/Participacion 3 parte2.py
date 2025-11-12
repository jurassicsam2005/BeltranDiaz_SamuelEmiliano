# Pide números hasta que el usuario escriba 0. Guarda los pares en una lista y los impares en otra. Al final, muestra cuantos números hay en cada lista. Ordena la lista en orden ascendente y recorre las listas para mostrar cada número uno por uno.
lista_numeros = []
lista_numeros_par =[]
lista_numeros_impar = []

while True:
    numero = int(input("Ingresa un numero (Ingresa 0 para terminar:) ")) 
    if numero == 0:
        break
    lista_numeros.append(numero)

for i in lista_numeros:
    if (lista_numeros % 2 == 0):
        lista_numeros_par.append(i)
    else:
        lista_numeros_impar.append(i)