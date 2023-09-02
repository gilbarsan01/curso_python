#Cifras pares e impares
#Generar un número aleatorio entero entre un millón y dos millones. Imprimir ese número en pantalla y decir cuántas cifras pares e impares tiene.


#Metodo por chatgpt
import random

# Genera un número aleatorio entre 1,000,000 y 2,000,000
numero_aleatorio = random.randint(1000000, 2000000)

# Imprime el número aleatorio generado
print("Número aleatorio:", numero_aleatorio)

# Convierte el número a una cadena para poder analizar cada dígito por separado
numero_str = str(numero_aleatorio)

# Inicializa contadores para cifras pares e impares
cifras_pares = 0
cifras_impares = 0

# Recorre cada dígito en la cadena del número
for digito in numero_str:
    if int(digito) % 2 == 0:  # Verifica si el dígito es par
        cifras_pares += 1  # Incrementa el contador de cifras pares
    else:
        cifras_impares += 1  # Incrementa el contador de cifras impares

# Imprime la cantidad de cifras pares e impares
print("Cifras pares:", cifras_pares)
print("Cifras impares:", cifras_impares)








#Método 1
#Generamos un número aleatorio entero, lo convertimos a cadena con str, recorremos sus valores con un bucle for y por cada elemento lo convertimos nuevamente en número con int para ver si se trata de un número par. Finalmente contamos los pares e imprimimos el resultado.
print ("===============Método 1==================")
from random import randint
x = randint(1000000, 2000001)
print(x)
x=str(x)
par=0
for i in x:
  if int(i)%2==0:
    par+=1
print('Hay un total de',par,'cifras pares')
print('Hay un total de',7-par,'cifras impares')



