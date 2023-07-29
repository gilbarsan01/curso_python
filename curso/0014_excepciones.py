#EXCEPCIONES

#La ejecucion de este bloque indica error al ejecutarlo.
#print (5 + '3')  #TypeError: unsupported operand type(s) for +: 'int' and 'str'




# Ejemplo de excepciones1
try:
    # Intenta realizar una operación aritmética no válida.
    # Esta línea está comentada para evitar un error en tiempo de ejecución.
    #print(5 + '3')

    # Intenta realizar una operación aritmética válida.
    print(5 + 3)

except:
    # Si ocurre una excepción, se ejecuta este bloque.
    # En este caso, si se descomentara la línea anterior, se produciría un error de tipo (TypeError).
    # Se imprimiría "Error sin terminar programa" indicando que ha ocurrido un error en la ejecución.
    print('Error sin terminar programa')

else:
    # Si no ocurre ninguna excepción, se ejecuta este bloque.
    # En este caso, si no hay errores, se imprimirá "Se ejecutó correctamente el programa".
    print('Se ejecutó correctamente el programa')

finally:
    # Este bloque siempre se ejecuta, ya sea que ocurra una excepción o no.
    # Se imprimirá una línea en blanco al final de la ejecución.
    print('Siempre se ejecutara este mensaje')





# Ejemplo de excepciones2
try:
    # Intenta imprimir una variable no definida, lo que generará un NameError.
    print(sdfdsg)

    # Intenta realizar una operación aritmética no válida.
    # Esta línea está comentada para evitar otro error en tiempo de ejecución.
    # print(5 + '3')

except NameError as errortypeNameError:
    # Si ocurre un NameError (variable no definida), se ejecuta este bloque.
    # Imprime "error de tipo NameError" y muestra información adicional sobre el error.
    print('error de tipo NameError')
    print(errortypeNameError)

except TypeError:
    # Si ocurre un TypeError (operación aritmética no válida), se ejecuta este bloque.
    # No se ejecutará en este ejemplo, ya que esa línea está comentada.
    print('error de tipo TypeError')

else:
    # Si no ocurre ninguna excepción, se ejecuta este bloque.
    # En este caso, no se ejecutará debido a que se produce un NameError.
    print('Se ejecutó correctamente el programa')

finally:
    # Este bloque siempre se ejecuta, ya sea que ocurra una excepción o no.
    # Se imprimirá "Siempre se ejecutará este mensaje" al final de la ejecución.
    print('Siempre se ejecutará este mensaje')


