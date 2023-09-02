#Bucles anidados
#Reto: Bucles anidados
#Generar la tabla de multiplicar.


#Mi metodo
for i in range(1,11):
    for j in range(1,11):
        print("",i,"x", j,"=", i*j)
    print("-----------------")




#Metodo 1
for i in range(1,11):
  for j in range (1,11):
    x=i*j
    print(i,'*',j,'=',x)
    if j == 10:
      print("_"*40)


#Metodo 2
for i in range(1,11):
  for j in range(1,11):
    print ('%d * %d = %d' % (i,j,i*j))
    if j == 10:
      print("_"*40)