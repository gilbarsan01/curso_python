#FUNCION isinstance : la función isinstance() es una función incorporada en Python que se utiliza para verificar si un objeto o valor pertenece a una clase o tipo específico. Su sintaxis es la siguiente:

# Ejemplo 1
x = 5
resultado = isinstance(x, int)
print(resultado)  # Output: True, porque x es un número entero (int).

# Ejemplo 2
y = "Hola"
resultado = isinstance(y, str)
print(resultado)  # Output: True, porque y es una cadena (str).

# Ejemplo 3
z = 3.14
resultado = isinstance(z, float)
print(resultado)  # Output: True, porque z es un número de punto flotante (float).

# Ejemplo 4
lista = [1, 2, 3]
resultado = isinstance(lista, list)
print(resultado)  # Output: True, porque lista es una lista (list).

# Ejemplo 5
tupla = (1, 2, 3)
resultado = isinstance(tupla, list)
print(resultado)  # Output: False, porque tupla no es una lista (list).


x = "valor"
resultado = isinstance(x, int)
