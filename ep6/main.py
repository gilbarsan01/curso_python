# print(5 < 10) #True
# print(2 > 20) #Falso
# print(6 <= 6) #True
# print (0 == 0) #True

'''
prom = input("pedir promedio")
si prom > 6 entonces
  aprueba
sino
  reprueba
'''

num1 = int(input("pedir primer numero "))
num2 = int(input("pedir segundo numero "))
num3 = int(input("pedir tercer numero "))

prom = (num1 + num2 + num3)/3

print("el promedio es %.2f"%prom)
if(prom > 6):
	print("aprobado")
else:
	print("reprobado")