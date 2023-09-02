#Máximo y mínimo
#Generar 10 números aleatorios y calcular el máximo y el mínimo.


#Metodo1

from random import randint

# Importa la función randint del módulo random
# Esto permite generar números aleatorios en el rango especificado

lista = []  # Inicializa una lista vacía
# Creará una lista para almacenar los números aleatorios generados en el bucle

for i in range(10):
    # Comienza un bucle que se ejecutará 10 veces
    # Esto generará 10 números aleatorios y los añadirá a la lista

    w = randint(1, 100)
    # Genera un número aleatorio entre 1 y 100 (incluyendo ambos)
    # El resultado se guarda en la variable w

    lista.append(w)
    # Agrega el número aleatorio generado a la lista

print(lista)
# Imprime la lista completa de números aleatorios generados

print('Máximo:', max(lista))
# Imprime el valor máximo de la lista utilizando la función max()
# Esto encuentra y muestra el número más grande en la lista

print('Mínimo:', min(lista))
# Imprime el valor mínimo de la lista utilizando la función min()
# Esto encuentra y muestra el número más pequeño en la lista





print("========Metodo2============")
from random import randint
x=0
lista=[]
while x<10:
  w=randint(1, 100)
  lista.append(w)
  x+=1
print(lista)
maxi=lista[0] #inicializamos el máximo con el primer elemento de la lista
mini=lista[0] #inicializamos el mínimo con el primer elemento de la lista
for i in range (10):
  if lista[i]>=maxi:
    maxi=lista[i]
  elif lista[i]<=mini:
    mini=lista[i]
print('El mayor es:',maxi)
print('El mmenor es:',mini)




print("========Metodo3============")
from random import randint
maxi=0
mini=100
for i in range(10):
  x=randint(1, 100)
  print(x)
  if x>=maxi:
    maxi=x
  elif x<=mini:
    mini=x
print('El mayor es: ',maxi)
print('El menor es: ',mini)






# Método 4
#Este método es similar al anterior si bien el cálculo del máximo y el mínimo no se realiza usando un condicional if sino que usamos las funciones max y min del propio Python.
print("========Metodo4============")
from random import randint

# Importa la función randint del módulo random
# Esto permite generar números aleatorios en el rango especificado

maxi = 0
# Inicializa la variable maxi con un valor inicial de 0
# Se utilizará para almacenar el valor máximo encontrado

mini = 100
# Inicializa la variable mini con un valor inicial de 100
# Se utilizará para almacenar el valor mínimo encontrado

for i in range(10):
    # Comienza un bucle que se ejecutará 10 veces
    # Esto generará 10 números aleatorios y verificará si son máximos o mínimos

    x = randint(1, 100)
    # Genera un número aleatorio entre 1 y 100 (incluyendo ambos)
    # El resultado se guarda en la variable x

    print(x)
    # Imprime el número aleatorio generado

    maxi = max(maxi, x)
    # Actualiza el valor máximo
    # La función max() compara el valor actual de maxi con x y devuelve el mayor

    mini = min(mini, x)
    # Actualiza el valor mínimo
    # La función min() compara el valor actual de mini con x y devuelve el menor

print('El mayor es:', maxi)
# Imprime el valor máximo encontrado después de recorrer el bucle

print('El menor es:', mini)
# Imprime el valor mínimo encontrado después de recorrer el bucle







#Método 5
#Creamos una lista que se basa en obtener una muestra de 10 elementos sin repetición elegidos de forma aleatoria entre los cien que contiene el rango que va entre 0 y 99. Imprimimos la lista desordenada, luego la ordenamos y la volvemos a imprimir ya ordenada. Para mostrar el mínimo y el máximo únicamente tenemos que elegir el primer y último elemento de la lista ordenada.
print("========Metodo5============")
import random

# Importa el módulo random, que se utilizará para generar números aleatorios y mezclar listas

L = random.sample(range(100), 10)
# Genera una muestra aleatoria de 10 números únicos entre 0 y 99 (rango 100)
# Esta muestra se almacena en la lista L

print(L)
# Imprime la lista L, que contiene la muestra aleatoria de números

L.sort()
# Ordena la lista L de forma ascendente
# La función sort() modifica la lista original en lugar de crear una nueva

print(L)
# Imprime la lista L nuevamente, pero esta vez estará en orden ascendente

print('Máximo:', L[9])
# Imprime el último elemento de la lista L, que es el máximo valor después de ordenar

print('Mínimo:', L[0])
# Imprime el primer elemento de la lista L, que es el mínimo valor después de ordenar
