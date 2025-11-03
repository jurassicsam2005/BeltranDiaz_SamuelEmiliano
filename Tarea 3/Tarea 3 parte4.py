#Haz un programa que sume todos los números impares del 1 al 50.

suma = 0

for i in range(1, 51):
    if i % 2 != 0:
        suma = suma + i

print(f"La suma de los numeros es {suma}")