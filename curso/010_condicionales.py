#CONDICIONALES


if 4 > 6:
    print('4 es menor que 6') #Imprime al entrar en la condicion


if 4 < 6:
    print('4 es menor que 6')   #Como no entra en la condicion no lo imprime


numero = 7      #Funcion para validar condicionales
if 4 > 6 or numero == 7:
    print('4 es mayor que 6 o nuemro es igual que 4')


valor = 'Este es un mensaje con bastante texto'   #Funcion para validar si el mensaje es mayor a 5 caracteres.
if len(valor) > 5:
    print('Este mensaje tiene mucho texto')



#Condicion con else
if 4 > 6:
    print('4 es menor que 6')
else:
    print('No se cumplio la condicion')



#Validacion con "elif" anidados
num1 = 6
if 3 > 6 :
    print('3 es menor que 6')
elif num1 == 7:
    print('num1 diferente 7')
elif num1 < 7:
    print('num1 menor que 7 :) ')
else:
    print('No se cumplio ninguna de las condicion ')
