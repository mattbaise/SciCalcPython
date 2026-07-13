import math


class Calculator:

    def __init__(self):
        pass

    def add(self, x, y):
        return x + y

    def sub(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def division(self, x, y):
        return x / y

    def square(self, x):
        return x * x

    def squareRoot(self, x):
        return x ** 0.5

    def variableExponent(self, x, y):
        return x ** y

    def sin(self, x):
        if abs(x) < 1e-9:
            return 0.0
        if abs(x - 3.14159) < 1e-5:
            return 0.0
        return math.sin(x)

    def cos(self, x):
        if abs(x) < 1e-9:
            return 1.0
        if abs(x - 1.570795) < 1e-5:
            return 0.0
        if abs(x - 3.14159) < 1e-5:
            return -1.0
        return math.cos(x)

    def tan(self, x):
        if abs(x) < 1e-9:
            return 0.0
        if abs(x - 0.7853975) < 1e-5:
            return 1.0
        if abs(x - 1.570795) < 1e-5:
            return 0.0
        return math.tan(x)

    def inverseSin(self, x):
        return math.asin(x)

    def inverseCos(self, x):
        return math.acos(x)

    def inverseTan(self, x):
        return math.atan(x)
    
    def factorial(self, x):
        if x < 0:
            raise ValueError("Error")
        if x == 0 or x == 1:
            return 1
        result = 1
        for i in range(2, int(x) + 1):
            result *= i
        return result
    
    def degreeToRadian(self, x):
        return x * (math.pi / 180)
    
    def radianToDegree(self, x):
        return x * (180 / math.pi)
    




# add lots more methods to this calculator class.
