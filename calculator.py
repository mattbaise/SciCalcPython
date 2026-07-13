class Calculator:

    def __init__(self):
        pass

    def init (self, state):
        self.state = state

    def add(self, x, y):
        return x + y

    def sub(self, x, y):
        return x - y

    def square(self, x):
        return(x * x)

    def sqrt(self, x):
        return x ** 0.5

    def exponent(self, x, y):
        return x ** y

    def inverse(self, x):
        if x == 0:
            print("Cannot take inverse of zero.")
            return 0
        return 1 / x

    def switchsign(self, x):
        if x == 0:
            print("Cannot switch sign of zero.")
            return 0
        return x * -1
def switchDisplayMode(self, mode):
        if mode == "DEG":
            self.angle_mode = "DEG"
        elif mode == "RAD":
            self.angle_mode = "RAD"
        else:
            print("Invalid mode. Please choose 'DEG' or 'RAD'.")

def M(self, value):
        self.memory = value     

def MC(self):
        self.memory = 0
        
def MRC(self):
        return self.memory  


# add lots more methods to this calculator class.
