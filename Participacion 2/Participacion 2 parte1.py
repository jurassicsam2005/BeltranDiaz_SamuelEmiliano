#Haz un programa en Python que pida un numero, posteriormente muestra todos los numeros desde 1 hasta el numero ingresado. Imprime un coteo de numeros pares y de numeros impares.
numero = int(input("Ingresa un numero: "))
pares = 0
impares = 0
for i in range(1, numero + 1):
    print(i)
    if i % 2 == 0:
        pares += 1
    else:
        impares += 1
print("Cantidad de numeros pares:", pares)
print("Cantidad de numeros impares:", impares)
