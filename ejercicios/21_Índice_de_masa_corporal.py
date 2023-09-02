#Longitud de una cadena
#Crear una función que calcule la longitud de una cadena alfanumérica. Crear otra función que dada una cadena devuelva el primer caracter en mayúsculas y el resto en minúsculas. Pasar una palabra por ambas funciones y dar el resultado.


#Metodo1
def BMI(a,p):  
   IMD=p/a**2  
   return(IMD)  
altura = float(input('Dime tu altura por favor') or 1.7)  
print('Altura=',altura,'m')  
peso = float(input('Dime tu peso por favor')or 60)   
print('Peso=',peso,'Kg')  
print('Tu Indice de Masa Corporal es',round(BMI(altura,peso),2))  


print('======================')
#metodo 2
def BMI(a,p):  
   IMD=p/a**2  
   return(IMD)  
altura = float(input('Dime tu altura por favor') or 1.7)  
print('Altura=',altura,'m')  
peso = float(input('Dime tu peso por favor')or 60)   
print('Peso=',peso,'Kg')  
ibc=round(BMI(altura,peso),2)  
print('Tu Indice de Masa Corporal es',ibc)  
if ibc<=16:  
  print("Tienes Delgadez Severa")  
elif ibc>16 and ibc<17:  
  print("Tienes Delgadez Moderada")  
elif ibc>=17 and ibc<18.50:  
  print("Tienes Delgadez Aceptable")  
elif ibc>=18.50 and ibc<25:  
  print("Tienes Peso Normal")  
elif ibc>=25 and ibc<30:  
  print("Tienes Sobrepeso")  
elif ibc>=30 and ibc<35:  
  print("Obeso: Tipo I")  
elif ibc>=35 and ibc<40:  
  print("Obeso: Tipo II")  
elif ibc>=40:  
  print("Obeso: Tipo III")  