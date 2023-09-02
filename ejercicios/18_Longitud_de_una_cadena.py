#Longitud de una cadena
#Crear una función que calcule la longitud de una cadena alfanumérica. Crear otra función que dada una cadena devuelva el primer caracter en mayúsculas y el resto en minúsculas. Pasar una palabra por ambas funciones y dar el resultado.


#Metodo1
def longitudCadena(x):
  contador=0
  for i in x:
    contador+=1
  return contador
def nombrePropio(x):
  y=x.lower()
  return y[0].upper()+y[1:]
x=input('Indique una palabra') or 'mADRId'
print(nombrePropio(x),'tiene',longitudCadena(x),'caracteres.')


print('=========================')
#Metodo2
def longitudCadena(x):
  return len(x)
def nombrePropio(x):
  return x.capitalize()
x=input('Indique una palabra:') or 'maDRid'
print(nombrePropio(x),'tiene',longitudCadena(x),'caracteres.') 