#Unir listas
#Generar primero una lista con los números entre 0 y 10, luego generar otra lista con los números del 11 al 20. Unir ambas lista e imprimir el resultado.


#Mi metodo:
list_01 = [ 0,1,2,3,4,5,6,7,8,9 ]
list_02 = [ 10,11,12,13,14,15,16,17,18,19,20 ]
list_01.append(list_02)
print(list_01)



print("=================")
#metodo1
list01=list(range(11))
list02=list(range(11,21))
list01.extend(list02)
print(list01)


print("=================")
#metodo2
miLista=list(range(11))
tuLista=list(range(11,21))
nuestraLista = miLista + tuLista
print(nuestraLista)