#DICCIONARIO:   Sirve para guardar elementos con valor.


my_dict = {'Nombre':'Gilberto',
           'Apellido':'Barraza',
           'Edad':'32 ',
           23:14}

print(type(my_dict)) #Imprime el valor del elemento.


print(my_dict['Nombre']) #Funcion para imprimir el valor dentro del diccionario.
print(my_dict['Edad'])   #Funcion para imprimir el valor dentro del diccionario.
print(my_dict[23])       #Funcion para imprimir el valor dentro del diccionario.
print(my_dict.keys())    #Funcion para imprimir todas las keys
print(my_dict.values())  #Funcion para imprimir todos los valores



my_dict =  list(my_dict)   #Funcion para convertir el diccionario a lista
print(type(my_dict))
print(my_dict)

my_dict = set(my_dict)     #Convertir la lista -> set
print(type(my_dict))
print(my_dict)

my_dict = tuple(my_dict)  #Convertir la set -> a tupla
print(type(my_dict))
print(my_dict)

