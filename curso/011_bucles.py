#BUCLE



#WHILE

#bucle con while 
numero = 0
while numero < 10:
    numero += 1
    print(numero)



#bucle con while,condicional y break
print ('------------')
numero = 0
while numero < 10:
    numero += 1
    print(numero)
    if numero == 5:
        print(' es igual que 5')
        break



#bucle con for
print ('------------')
lista = [4,8,9,5.0,20,45]
for number in lista:
    print(number)




#bucle for con range
print ('------------')
# Ejemplo con un argumento
for i in range(5):
    print(i, end=", ") # prints: 0, 1, 2, 3, 4, 


#bucle con for
print ('------------')
# Ejemplo con un argumento
for e in range(8):
    print(e) 
