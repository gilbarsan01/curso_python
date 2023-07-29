#FUNCIONES

# 01 - Se define una función sencilla
def Func_simple():
    """
    Esta función imprime el mensaje "Hola función".
    No recibe argumentos ni devuelve valores.
    """
    print('Hola función')

# Se manda a ejecutar la función
Func_simple()


# 02 - Función básica para sumar 2 números:
def Sum_numeros(num1, num2=10):
    """
    Esta función suma dos números y luego imprime el resultado.
    Si solo se proporciona un argumento (num1), el valor predeterminado para num2 es 10.
    
    Parámetros:
    num1 (int or float): El primer número a sumar.
    num2 (int or float, opcional): El segundo número a sumar (valor predeterminado: 10).

    Retorna:
    int or float: La suma de num1 y num2.
    """
    result = num1 + num2
    print(result)
    return result

# Ejemplos de llamadas a la función Sum_numeros
Sum_numeros(6, 3)    # Resultado: 9 (6 + 3)
Sum_numeros(6)       # Resultado: 16 (6 + 10, ya que num2 toma el valor predeterminado)
totalsum = Sum_numeros(6, 8)
# Resultado: 14 (6 + 8). La función imprime este resultado y también se asigna a la variable 'totalsum'.

print(totalsum)      # Imprime el valor de 'totalsum', que es 14 (el resultado de la última llamada a Sum_numeros).




def Sum_numerosv2(number1, number2=10):
    print( number1 + number2)
    return number1 + number2


def Sum_three_numbers(num01,num02,num03):
    print( num01 +  num02 + num03)

def multiplica2num(n1,n2):
    print( n1 * n2)