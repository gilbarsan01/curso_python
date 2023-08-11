#Reto 8 :Pares
#Listar los números pares del 10 al 20.


#Mi metodo:
valor=10
while (valor <= 20 ):
  if valor % 2 == 0:
      print(valor)
  valor+=1
  

print ("============")
#metodo 2:
for x in range(10, 21, 2):
  print(x)


print ("============")
#Método 3
#Usando listas de comprensión (List Comprehensions).

print([i for i in range(10,21) if i%2==0])
