# Programa que calcula cuántos números del 1 al 100 son divisibles entre 3 y entre 5.

# Contadores para cada tipo de número
div_por_3 = 0
div_por_5 = 0
div_por_ambos = 0

# Revisar números del 1 al 100
for numero in range(1, 101):
    # Verificar divisibilidad por 3
    if numero % 3 == 0:
        div_por_3 = div_por_3 + 1
    
    # Verificar divisibilidad por 5
    if numero % 5 == 0:
        div_por_5 = div_por_5 + 1
    
    # Verificar divisibilidad por ambos
    if numero % 3 == 0:
        if numero % 5 == 0:
            div_por_ambos = div_por_ambos + 1

# Mostrar resultados
print(f"Números divisibles entre 3: {div_por_3}")
print(f"Números divisibles entre 5: {div_por_5}")
print(f"Números divisibles entre 3 y 5: {div_por_ambos}")

