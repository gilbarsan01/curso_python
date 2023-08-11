#Funciones
#Crear una función que calcule el cuadrado de un número. Probar la función con los números entre -10 y +10. Crear otra función que lo único que hace es imprimir al final la frase “Programa finalizado”. Ejecutar ambas funciones.


#Mi metodo
def calcularcuadrado(number):
    resultado = (number * number)
    print(resultado)
    # return resultado

def saludo():
    print("Se finalizo el mensaje")

calcularcuadrado(10)
saludo()



print("============")
#Otro metodo:
z=-10
def cuadrado(n):
  y=n**2
  return(y)
def fin():
  x=('Programa finalizado')
  return(x)
while z<11:
  print(cuadrado(z))
  z+=1
print(fin())


print("============")
#Otro metodo:
def cuadrado2(z):
  resultado=[]
  for i in range(-z,z+1):
    resultado.append(i**2)
  return(resultado)
def fin():
  print('Programa finalizado')
print(cuadrado2(10))
fin()
