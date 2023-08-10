#from random import randrange, choice, randint
import random

#Imprime numero random del 0 al 10.
#print(randrange(10))

#print(choice(["uno", "dos", "tres"]))






numero_aleatorio = random.randint(1, 120)

print("Número aleatorio:", numero_aleatorio)

if 10 <= numero_aleatorio <= 50:
    print("El número está en el intervalo entre 10 y 50.")
elif 50 < numero_aleatorio <= 100:
    print("El número es mayor que 50 y está hasta 100.")
elif numero_aleatorio > 100:
    print("El número es mayor que 100.")
elif numero_aleatorio < 10:
    print("El número es menor que 10.")
