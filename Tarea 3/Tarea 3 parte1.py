#Haz un programa que calcule cuántos números del 1 al 100 son divisibles entre 3 y entre 5.

def contar_divisibles(inicio=1, fin=100):
	"""Devuelve una tupla (cantidad_div3, cantidad_div5, cantidad_ambos).

	inicio, fin: rangos inclusivos.
	"""
	cantidad_div3 = sum(1 for n in range(inicio, fin + 1) if n % 3 == 0)
	cantidad_div5 = sum(1 for n in range(inicio, fin + 1) if n % 5 == 0)
	cantidad_ambos = sum(1 for n in range(inicio, fin + 1) if n % 3 == 0 and n % 5 == 0)
	return cantidad_div3, cantidad_div5, cantidad_ambos


def main():
	div3, div5, ambos = contar_divisibles(1, 100)
	print(f"Números del 1 al 100 divisibles entre 3: {div3}")
	print(f"Números del 1 al 100 divisibles entre 5: {div5}")
	print(f"Números del 1 al 100 divisibles entre 3 y 5 (ambos): {ambos}")


if __name__ == "__main__":
	main()

