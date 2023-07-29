#SETS:  Es similar a una lista, pero diferente.

my_set = {}             #Asi lo detecta como un diccionario
print(type(my_set))


my_set = {'Prython', 'JavaScript', 'C++'}
print(type(my_set))

print(my_set)


#print(my_set(0))     Esto marca error ya que no es una lista, si no un diccionario.

my_set.add('C++') #Funcion para agregar elemento, pero para que se añada un elemento tiene que ser diferente por ende seguira siendo el mismo diccionario.
print(my_set)


my_set.add('Nuevo_campo') #Funcion para agregar elemento, pero para que se añada un elemento tiene que ser diferente por ende seguira siendo el mismo diccionario.
print(my_set)


my_set_0 = {'Prython', 'JavaScript', 'C++'}


my_set.difference_update(my_set_0) #Funcion para comparar 2 diccionarios y la variable tendra el nuevo valor que sea diferente entre los 2 diccionarios.
print(my_set)



