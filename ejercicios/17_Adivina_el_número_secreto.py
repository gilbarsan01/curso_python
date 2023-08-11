#Adivina el número secreto
#Se genera un número aleatorio entero entre 1 y 100. El usuario debe adivinar el número secreto, diciendo en cada tirada si es mayor o menor.


import random
n=random.randrange(1,100)
nu=int(input('Dime el número que crees que he elegido: '))
while nu!=n:
    if nu>n:
        nu=int(input('El número es mas pequeño, intenta de nuevo:'))
    elif nu<n:
        nu=int(input('El número es mas GRANDE, intenta de nuevo:'))
print('Felicidades has adivinado que el número secreto es:',n)