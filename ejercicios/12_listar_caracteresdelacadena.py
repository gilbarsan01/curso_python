#Cadenas alfanuméricas
#Listar los caracteres de la cadena ‘2001: A Space Odyssey’.


#Mi metodo
cadena='2001: A Space Odyssey'
for i in cadena:
    print(i)


print("======================")
#metodo1:
frase='2001: A Space Odyssey'
i=0
while i < len(frase):
    print(frase[i])
    i+=1


print("======================")
#metodo2:
mifrase='2001: A Space Odyssey'
mylist=list(mifrase)
for z in mylist:
    print(z)