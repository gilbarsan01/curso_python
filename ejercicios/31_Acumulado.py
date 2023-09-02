#Listar los números entre 1 y 10. En la columna contigua sus cuadrados, y en la tercera columna sus cubos. Al final dar la suma de todos los valores de cada columna.



#metodo1
s1=0
s2=0
s3=0
for i in range(1,11):
    s1=s1+i
    s2=s2+i**2
    s3=s3+i**3
    print(i,i**2,i**3)
print('_'*15)
print(s1,s2,s3)









#metodo2
print('===========metodo2==========')
# Inicializa las variables para las sumas de números, cuadrados y cubos
s1 = s2 = s3 = 0

# Itera a través de los números del 1 al 10
for i in range(1, 11):
    # Calcula el cuadrado y el cubo del número actual
    j = pow(i, 2)
    k = pow(i, 3)
    
    # Agrega el número actual, su cuadrado y su cubo a las sumas acumulativas
    s1 += i
    s2 += j
    s3 += k
    
    # Imprime el número actual, su cuadrado y su cubo en una línea
    print(i, j, k)

# Imprime una línea de guiones bajos para separar
print('_' * 11)

# Imprime las sumas acumulativas de los números, cuadrados y cubos
print(s1, s2, s3)






#metodo3
print('===========metodo3==========')
# Inicializa tres listas vacías para almacenar los números, cuadrados y cubos
a = list()
b = list()
c = list()

# Itera a través de los números del 1 al 10
for i in range(1, 11):
    # Calcula el cuadrado y el cubo del número actual
    j = pow(i, 2)
    k = pow(i, 3)
    
    # Agrega el número actual, su cuadrado y su cubo a las listas respectivas
    a.append(i)
    b.append(j)
    c.append(k)
    
    # Imprime el número actual, su cuadrado y su cubo en una línea
    print(i, j, k)

# Imprime una línea de guiones bajos para separar
print('_' * 11)

# Imprime las sumas de los elementos en las listas a, b y c utilizando la función sum()
print(sum(a), sum(b), sum(c))