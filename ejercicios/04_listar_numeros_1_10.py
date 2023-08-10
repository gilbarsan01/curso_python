#Bucles
#Listar los números del 1 al 10.

#Pueden ser varios metodos:

#Metodo1
x=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(x)

#Metodo2:
miLista=list(range(1,11))
print(miLista)


#Metodo3
valor=0
while (valor < 10):
  valor+=1
  print(valor)

#Metodo4
for x in range(1,11):
  print (x)


#Metodo5                             
y=[i+1 for i in range(10)]
print(y)

 