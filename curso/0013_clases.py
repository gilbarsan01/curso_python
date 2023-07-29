#CLASES


class Humano:
    def __init__(self, altura, edad, peso):
        """
        Clase Humano que representa a una persona con atributos de altura, edad y peso.

        Parámetros:
        altura (float): La altura del humano en metros.
        edad (int): La edad del humano en años.
        peso (float): El peso del humano en kilogramos.
        """
        self.altura = altura
        self.edad = edad
        self.peso = peso
    
    def comer(self):
        """
        Método que simula la acción de comer para el humano.

        Imprime un mensaje que indica que el humano está comiendo y muestra su edad.
        """
        print(f'El humano de {self.edad} años está comiendo...')

# Creación de una instancia de la clase Humano con valores específicos para altura, edad y peso.
humano_1 = Humano(1.72, 32, 80)

# Imprimir información sobre el humano_1.
print(f'El humano1 tiene una altura de {humano_1.altura} metros, tiene una edad de {humano_1.edad} años y pesa {humano_1.peso} kilogramos.')

# Llamar al método comer() para el objeto humano_1.
humano_1.comer()
