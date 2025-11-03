# Programa que simula una calculadora básica con opciones de suma, resta, multiplicación y división

# Variable para controlar el ciclo principal
seguir = True

while seguir:
    # Mostrar menú
    print("\n=== Calculadora Básica ===")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")
    
    # Obtener opción del usuario
    opcion = input("\nSeleccione una opción (1-5): ")
    
    # Procesar la opción
    if opcion == "1":
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        resultado = num1 + num2
        print(f"\n{num1} + {num2} = {resultado}")
        
    if opcion == "2":
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        resultado = num1 - num2
        print(f"\n{num1} - {num2} = {resultado}")
        
    if opcion == "3":
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        resultado = num1 * num2
        print(f"\n{num1} × {num2} = {resultado}")
        
    if opcion == "4":
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        if num2 != 0:
            resultado = num1 / num2
            print(f"\n{num1} ÷ {num2} = {resultado}")
        else:
            print("\nError: No se puede dividir entre cero")
            
    if opcion == "5":
        print("\n¡Gracias por usar la calculadora!")
        seguir = False
        
    if opcion != "1" and opcion != "2" and opcion != "3" and opcion != "4" and opcion != "5":
        print("\nOpción no válida. Por favor, seleccione una opción del 1 al 5.")
