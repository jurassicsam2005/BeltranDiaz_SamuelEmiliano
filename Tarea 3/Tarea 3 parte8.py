#Pide dos números y muestra todos los números entre ellos que sean múltiplos de 7.

numero1 = int(input("Ingresa el primer numero"))
numero2 = int(input("Ingresa el segundo numero"))

for i in range(numero1, numero2  + 1):
    if i % 7 == 0:
        print(i)