#Haz un programa en Python que pida al usuario ingresar un número, y muestre su tabla de multiplicar del 1 al 20, pero solo para los múltiplos pares (Es decir, numero x 2, número x 4, número x 6, etc).

numero = int(input("ingresa un numero"))
resultado = 0

for i in range(1, 21):
    if i % 2 == 0: 
        resultado= numero * i 
        print(f"{numero} x {i} = {resultado}")


  
