#Series
#Listar los números entre un valor inicial y uno final, con un cierto intervalo. Al final dar la suma de todos los valores listados.


#Mi metodo
v_inicial=10
v_fin=20
intervalo=2
total=0
for x in range(v_inicial,v_fin,intervalo):
    print(x)
    total+=x
print("total", total)


print("=============")
#Metodo1
#lista
x=list(range(0,10,3))
print(x)
print(sum(x))
