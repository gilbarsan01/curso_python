


#STRING
primer_string = "primer_Mensaje"
segundo_string = 'segundo_Mensaje'

#Primer manera (No recomendable)
print('Esto es un mensaje' + ' '+ primer_string + ' '+segundo_string)

#Segunda forma recomendada
print(f'Este mensaje es recomendado {primer_string} {segundo_string}')


other_string =  'hola'

a,b,c,d = other_string

print(a)
print(b)
print(c)
print(d)

print(f'{a}{b}{c}{d}')


#FUNCIONES CON STRING
print(primer_string.upper())        #Funcion para convertir todo el texto en MAYUSCULAS
print(primer_string.capitalize())   #Funcion para colocar la primera letra en mayuscula
print(primer_string.lower())        #Funcion para convertir todo el texto en minusculas
print(len(primer_string))           #Funcion para contar los caracteres de la variable
print(primer_string.find('r'))      #Funcion para encontrar en que posicion se encuentra la letra , 0, 1, 2, 3
print(primer_string.find('e'))      #Funcion para encontrar en que posicion se encuentra la letra , 0, 1, 2, 3
print(primer_string.count('e'))     #Funcion para contar cuantas veces se encuentra la letra
print(primer_string.upper().isupper()) #Se pueden realizar 2 funciones al mismo tiempo, primero convierte todas en mayusculas y con la segunda validacion si todas son MAYUSCULAS por tal motivo retorna resultado en boleano Tre

print(primer_string.upper().islower()) #Se pueden realizar 2 funciones al mismo tiempo, primero convierte todas en mayusculas y con la segunda validacion si todas son MAYUSCULAS por tal motivo retorna resultado en boleano False
