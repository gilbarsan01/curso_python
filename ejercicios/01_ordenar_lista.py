#Ejercucio: Ordenar lista de elementos.
#Obtener lista de elelemtos y ordenar los elementos en su lista correspondiente.


def separate_numbers_and_characters(input_list):
    """
    Función que toma una lista de entrada y separa los números y caracteres en listas diferentes.

    Parámetros:
        input_list (list): Lista que contiene números y caracteres.

    Retorna:
        tuple: Una tupla que contiene dos listas, la primera con los números encontrados
               en la lista de entrada y la segunda con los caracteres encontrados.
    """
    numbers_list = []
    characters_list = []
    

    for item in input_list:
        if isinstance(item, int) or isinstance(item, float):
            # Si el elemento es un número (int o float), lo agregamos a la lista de números.
            numbers_list.append(item)
        elif isinstance(item, str):
            # Si el elemento es una cadena (carácter), lo agregamos a la lista de caracteres.
            characters_list.append(item)

    return  numbers_list, characters_list 


# Ejemplo de lista que contiene números y caracteres
input_list = [2000, 1, 'a', 2, 'b', 3.14, 'c', 4, 'd', 'e'  , 'saludo' , 1000]

# Llamada a la función para separar los números y caracteres
numbers, characters = separate_numbers_and_characters(input_list)

# Imprimir las listas resultantes
print("Lista de números:", numbers)
print("Lista de caracteres:", characters)


