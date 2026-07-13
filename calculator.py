class Calculator:

    def __init__(self):
        self.memory = 0.0
        self.angle_mode = "DEG"

    def init(self, state):
        self.state = state

    def add(self, x, y):
        return x + y

    def sub(self, x, y):
        return x - y

    def divide(self, x, y):
        if y == 0:
            raise ValueError("Cannot divide by zero.")
        return x / y

    def square(self, x):
        return x * x

    def sqrt(self, x):
        if x < 0:
            raise ValueError("Cannot take square root of negative number.")
        return x ** 0.5

    def exponent(self, x, y):
        return x ** y

    def inverse(self, x):
        if x == 0:
            raise ValueError("Cannot take inverse of zero.")
        return 1 / x

    def switchsign(self, x):
        return x * -1

    def switchDisplayMode(self, mode):
        if mode == "DEG":
            self.angle_mode = "DEG"
        elif mode == "RAD":
            self.angle_mode = "RAD"
        else:
            raise ValueError("Invalid mode. Please choose 'DEG' or 'RAD'.")

    def M(self, value):
        self.memory = value

    def MC(self):
        self.memory = 0.0

    def MRC(self):
        return self.memory

# add lots more methods to this calculator class.
