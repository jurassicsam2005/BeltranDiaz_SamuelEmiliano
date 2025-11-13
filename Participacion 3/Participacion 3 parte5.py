# Haz un programa que pida un número, y crea una nueva lista sin duplicados. Pide 10 números.
lista_numeros = [] 

num = int(input(f"Introduce el número: "))
if num not in lista_numeros:
    lista_numeros.append(num)

print("Lista sin duplicados:", lista_numeros)
