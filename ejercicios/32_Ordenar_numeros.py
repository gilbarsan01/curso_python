#Imprimir una lista de 10 números aleatorios sin repetición que varíen en el rango 80 a 99. Volver a imprimir la lista pero ordenada.





import random

# Generar una lista de 10 números aleatorios sin repetición en el rango 80 a 99
random_numbers = random.sample(range(80, 100), 10)

print("Lista de números aleatorios sin repetición:")
print(random_numbers)

# Ordenar la lista
sorted_numbers = sorted(random_numbers)

print("\nLista ordenada:")
print(sorted_numbers)
