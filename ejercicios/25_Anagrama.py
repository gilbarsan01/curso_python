#Reto: Palíndromos

"""Reto: Anagramas
Crear una función que detecte si dos palabras son anagramas.

Dada una palabra, si reordenamos sus letras obtendremos un anagrama de ella. Por ejemplo, Roma es un anagrama de Amor y viceversa. Otros ejemplos de anagramas son:

saco -cosa
frase - fresa
Eva - ave
Marta - trama - matar
amor - ramo - Roma - mora
valora - Álvaro
riesgo - Sergio
poder - Pedro
delira - lidera
raza -azar
alma - mala - lama
rica - cría
aire - reía
gato - gota - toga
Ernesto - eternos - estreno - enteros """



"""Método 1
Vamos a crear una función que nos diga con True o False si dos palabras son o no son un anagrama una de la otra.


Convertimos las palabras a minúsculas y las convertimos en listas de caracteres. De esta forma la palabra Roma se convierte en la lista:

['r', 'o', 'm', 'a']

Luego se ordena de menor a mayor con sort(). De esta forma, haciendo este proceso en las dos palabras, si coinciden las listas ordenadas quiere decir que contienen los mismos caracteres. Esto nos permite asegurar que las palabras son anagramas la una de la otra."""

def anagrama(cadena1, cadena2):  
    cadena1lista = list(cadena1.lower())  # Convertir cadena1 a minúsculas y crear una lista de caracteres
    cadena2lista = list(cadena2.lower())  
    cadena1lista.sort()        # Ordenar la lista de caracteres de cadena1
    cadena2lista.sort()        
    return cadena1lista == cadena2lista  # Comparar las listas ordenadas, devuelve True si son iguales

palabra1 = 'Roma'  
palabra2 = 'amor'  
# Utilizar el método 'format()' para imprimir los resultados
print("¿Son anagramas {} y {}?: ".format(palabra1, palabra2), anagrama(palabra1, palabra2))




"""Método 2
Vamos a eliminar los acentos o tildes de las palabras antes de trabajar con ellas.
Hemos creado una función denominada normalizar que elimina los acentos (tildes) de las letras vayan en mayúsculas o en minúsculas.

El método 1 no detectaría que Álvaro y valora son anagramas, pero el método 2 si nos responde True. Se basa en el uso de la función replace."""


# Definición de la función 'normalizar' para reemplazar caracteres acentuados por caracteres sin acento
def normalizar(s):
    parejas = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )
    for a, b in parejas:
        # Reemplazar tanto caracteres minúsculos como mayúsculos con y sin acento
        s = s.replace(a, b).replace(a.upper(), b.upper())
    return s

# Definición de la función 'anagrama' para verificar si dos cadenas son anagramas
def anagrama(cadena1, cadena2):
    cadena1 = normalizar(cadena1)  # Normalizar cadena1 eliminando acentos
    cadena2 = normalizar(cadena2)  # Normalizar cadena2 eliminando acentos
    cadena1lista = list(cadena1.lower())  # Convertir cadena1 a minúsculas y crear una lista de caracteres
    cadena2lista = list(cadena2.lower())  # Convertir cadena2 a minúsculas y crear una lista de caracteres
    cadena1lista.sort()  # Ordenar la lista de caracteres de cadena1
    cadena2lista.sort()  # Ordenar la lista de caracteres de cadena2
    return cadena1lista == cadena2lista  # Comparar las listas ordenadas, devuelve True si son iguales

# Definición de las palabras a verificar si son anagramas
palabra1 = 'Álvaro'
palabra2 = 'valora'

# Imprimir el resultado de la verificación utilizando la función 'anagrama'
print("¿Son anagramas {} y {}?: ".format(palabra1, palabra2), anagrama(palabra1, palabra2))
