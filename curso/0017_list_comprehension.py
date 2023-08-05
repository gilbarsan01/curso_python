#LIST_COMPREHEINSON

# Creando una lista 'lista_normal' con elementos del 1 al 7
lista_normal = [1, 2, 3, 4, 5, 6, 7]
print(lista_normal)  # Imprime la lista [1, 2, 3, 4, 5, 6, 7]

# Utilizando una lista de comprensión para crear una lista 'list_comprehension' con números del 0 al 6
list_comprehension = [i for i in range(7)]
print(list_comprehension)  # Imprime la lista [0, 1, 2, 3, 4, 5, 6]


# Utilizando una lista de comprensión para crear una lista 'list_comprehension' con cada carácter de la cadena 'mensaje'
mensaje = 'bienvenido'
list_comprehension = [i for i in mensaje]
print(list_comprehension)  # Imprime la lista ['b', 'i', 'e', 'n', 'v', 'e', 'n', 'i', 'd', 'o']


# Utilizando una lista de comprensión para crear una lista 'list_comprehension' con cada número del rango [0, 6] multiplicado por 2
list_comprehension = [i * 2 for i in range(7)]
print(list_comprehension)  # Imprime la lista [0, 2, 4, 6, 8, 10, 12]


# Utilizando una lista de comprensión para crear una lista 'list_comprehension' con el cuadrado de cada número del rango [0, 6]
list_comprehension = [i * i for i in range(7)]
print(list_comprehension)  # Imprime la lista [0, 1, 4, 9, 16, 25, 36]



# Definición de la función 'sum_number' que suma 10 a un número y se aplica en una lista de comprensión
def sum_number(number):
    number += 10
    return number
# Utilizando una lista de comprensión para aplicar la función 'sum_number' a cada número del rango [0, 6]
list_comprehension = [sum_number(i) for i in range(7)]
print(list_comprehension)  # Imprime la lista [10, 11, 12, 13, 14, 15, 16]



# Definición de la función 'sum_number' que agrega un guion bajo al final de un texto y se aplica en una lista de comprensión
def sum_number(number):
    number += "_"
    return number

mensaje = 'bienvenido'
# Utilizando una lista de comprensión para aplicar la función 'sum_number' a cada carácter de la cadena 'mensaje'
list_comprehension = [sum_number(i) for i in mensaje]
print(list_comprehension)  # Imprime la lista ['b_', 'i_', 'e_', 'n_', 'v_', 'e_', 'n_', 'i_', 'd_', 'o_']
