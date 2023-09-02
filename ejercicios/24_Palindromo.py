#Reto: Palíndromos
#Dada una cadena decir si es un palíndromo.

#Mi metodo:
print("================Mimetodo==============")
palabra = list(input("escribe la palabra:"))

list1 = list(palabra)
print(list1)
print("valor1:",list1)


list2= list(palabra)
list2.reverse()
print("valor2:",list2)

if list1 == list2:
    print("La palabra SIIIII es un polindromo:", palabra)
else:
    print("La palabra NOOOO es un polindromo:",palabra)





#Método 1: Pedimos al usuario una palabra y la convertimos a minúsculas. Por ejemplo, Radar se transforma en radar y ahora comparamos el primer caracter con el último, el segundo con el anteúltimo y así sucesivamente. Pero no es necesario comparar todos, es suficiente con comparar la mitad de ellos para no duplicar trabajo.
print("================metodo1==============")
def esPalindromo(palabra):  
 for i in range(0,int(len(palabra)/2)): #Es suficiente con analizar la mitad  
  if palabra[i]!=palabra[-i-1]:
   return False
 return True
palabra=input('Escriba una palabra: ').lower()  
print(palabra, '¿es un palindromo?',esPalindromo(palabra))  




#Método 2:Pedimos al usuario una palabra y la convertimos en una lista. Distinguimos dos casos según la longitud de la palabra sea par o impar.
print("================metodo2==============")
y=input('Dime una palabra: ')
x=list(y)
z=len(x)
i=z/2
if z%2==0:
  m=x[0:int(i)]
  m.reverse()
  q=x[int(i):int(z)]
  if m==q:
    print('Es un Palíndromo')
  else:
    print('No es un Palíndromo')
else:
  h=(z/2)-0.5
  m=x[0:int(h)]
  m.reverse()
  q=x[int(h+1):int(z)]
  if m==q:
    print('Es un Palíndromo')
  else:
    print('No es un Palíndromo')






#Método 3 Pedimos una palabra al usuario y convertimos todos sus caracteres en minúsculas. Esto se hace para que al poner por ejemplo Menem nos diga que si es un palíndromo. Para hacer el reverso del string y lo más sencillo es hacer y[::-1]. De esta forma al comparar una cadena alfanumérica con su reverso si son iguales entonces sabemos que se trata de un palíndromo.
print("================metodo3==============")
y=input('Dime una palabra: ').lower()
print("valor al reves:", y[::-1])
if y==y[::-1]:
  print('Es un Palíndromo')
else:
  print('No es un Palíndromo')


#Metodo5:Usamos una variable booleana de control.
print("================metodo5==============")
p=input('Dime una palabra: ').lower()
es=True
for i in range(len(p)):
  if p[i]!=p[len(p)-i-1]:
    es=False
if es:
  print('Si es un palíndromo')
else:
  print('No es un palíndromo')



#Método 6 : Utilizamos ''.join(reversed(x)) para darle la vuelta a x y darle ese valor a y.
print("================metodo6==============")
x=input('Dime una palabra: ').lower()  
y=''.join(reversed(x))
if y==x:
 print('Es un Palíndromo')
else:
 print('No es un Palíndromo')



#Método 7: Invierte el orden de los elementos de la lista z.
print("================metodo7==============")
y=input('Dime una palabra: ').lower()
x=list(y)
z=list(x)
z.reverse()
if z==x:
 print('Es un Palíndromo')
else:
 print('No es un Palíndromo')