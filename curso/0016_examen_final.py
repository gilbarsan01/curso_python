#MODULOS


# Importar el módulo funciones y llamar a la función Sum_numeros
import funciones
funciones.Sum_numeros(10, 20)
funciones.Sum_three_numbers(30,30,30)

print('----------------------------------------')
# Importar la función Sum_numerosv2 directamente y llamarla con diferentes argumentos
from funciones import Sum_numerosv2,Sum_three_numbers
Sum_numerosv2(10, 20)
Sum_numerosv2(50, 50)
Sum_three_numbers(40,40,40)


print('----------------------------------------')
# Importar la función multiplica2num del módulo funciones y darle un alias "mul2numbers"
from funciones import multiplica2num as mul2numbers
# Llamada a la función multiplica2num con argumentos 2 y 4 utilizando el alias "mul2numbers"
mul2numbers(2, 4)



