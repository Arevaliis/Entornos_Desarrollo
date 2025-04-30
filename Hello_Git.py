import math

print("*** Calculadora ****")

class Calculadora():
    """Es una clase imitando una calculadora"""

    def sumar(x,y):
        return x + y

    def resta(x,y):
        return x- y

    def multiplicacion(x, y):
        return x * y

    def division(x,y):
        return x/y

    def raiz(x):
        return math.sqrt(x)

    def potencia(x):
        return x**2

calculadora = Calculadora()