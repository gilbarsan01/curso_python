#LISTAS

my_list = ['Hola',34, False, "Hola mundo", 34] #Las listas deben de contener valores validos.


print(type(my_list))    #Imprime el tipo de valor
print(my_list)          #Imprime la lista completa

#Para imprimir los valores se empieza del 0,1,3,4,5..  ó -1,-2,-3
print(my_list[2])       #Imprime el valor en la posicion 2
print(my_list[-1])       #Imprime el ultimo valor.


#FUNCIONES
my_list.append('que onda')  #Funcion para agregar elemento a la lista
print(my_list)

my_list.insert(3, 'add_value') #Funcion para agregar elemento indicando la posicion en donde añadir.
print(my_list)

my_list.remove('Hola')   #Funcion para renover el primer valor en coincidencia.
print(my_list)

my_list.pop(2)   #Funcion para eliminar elemento indicando la posicion.
print(my_list)

print(my_list.count(34)) #Funcion para contar cuantas veces aparece el valor indicado.

my_list.reverse() #Funcion para imprimir la lista al reves.
print(my_list)

my_list.clear() #Funcion para borrar la lista
print(my_list)