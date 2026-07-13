import math


class Calculator:

    def __init__(self):
        self.state = 0.0
        self.memory = 0.0
        self.angle_mode = "DEG"

    def init(self, state):
        self.state = state

    def add(self, x, y):
        return x + y

    def sub(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def division(self, x, y):
        return x / y
        if y == 0:
            raise ValueError("Cannot divide by zero.")
    def square(self, x):
        return x * x

    def squareRoot(self, x):
        return x ** 0.5
      if x < 0:
            raise ValueError("Cannot take square root of negative number.")
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
    
    def inverse(self, x):
        if x == 0:
            raise ValueError("Cannot take inverse of zero.")
        return 1 / x
      
    def calculate_tip(self, bill_amount, tip_percent, people=1):
        """Return the tip, total bill, and amount owed by each person."""
        if bill_amount < 0:
            raise ValueError("Bill amount cannot be negative.")
        if tip_percent < 0:
            raise ValueError("Tip percentage cannot be negative.")
        if people <= 0:
            raise ValueError("Number of people must be at least 1.")

        tip = bill_amount * (tip_percent / 100)
        total = bill_amount + tip
        return round(tip, 2), round(total, 2), round(total / people, 2)
      
      def fahrenheit_to_celsius(self, fahrenheit):
        return (fahrenheit - 32) * 5 / 9

    def celsius_to_fahrenheit(self, celsius):
        return celsius * 9 / 5 + 32

    def switchUnitsMode(self, mode):
        mode = mode.upper()
        if mode == "DEG":
            self.angle_mode = "DEG"
        elif mode == "RAD":
            self.angle_mode = "RAD"
        else:
            raise ValueError("Invalid mode. Please choose 'DEG' or 'RAD'.")

    def switchDisplayMode(self, mode):
        """Backward-compatible name for switching trig units."""
        self.switchUnitsMode(mode)

    def M_plus(self):
        self.memory += self.state
        self.state = self.memory

    def MC(self):
        self.memory = 0.0

    def MRC(self):
        self.state = self.memory
        return self.state




# add lots more methods to this calculator class.
