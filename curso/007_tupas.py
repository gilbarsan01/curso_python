#TUPLAS: Son similares que las listas, solo que las listas tienen mas funciones. 
#En las tuplas no se puede añadir o eleminar elementos dentro de la tupla. Pero si podemos cambiar una variable por otra variable para convertirla en lista :) 

my_tupla = (53, 'Animal',7.5, 5, 7.5, True)    #Declaracion de tupla
print(type(my_tupla))               #type imprime el tipo de elemento que es.


print(my_tupla[0])          #Imprime la posicion 0 de la tupla
print(my_tupla.count(7.5))  #Imprime cuantos elemtos existen
print(my_tupla.index(True)) #Funcion index encontrar posicion en la que se encuentra el elemento.




my_tupla = list(my_tupla) #Funcion list para convertir la typla en lista  (Es decir  typado debil para cambiar la tupla a la variable lista.)
print(type(my_tupla))

my_tupla.pop()      #funcion para quitar el ultimo elemento de la lista.
print(my_tupla)



my_tupla = tuple(my_tupla) #Funcion list para convertir la lista en tupla  (Es decir  typado debil para cambiar la list a la variable tupla.)
print(type(my_tupla))
print(my_tupla)