from calculator import Calculator

def getTwoNumbers():
    a = float(input("first number? "))
    b = float(input("second number? "))
    return a, b

def getOneNumber():
    a = float(input("number? "))
    return a

def displayResult(x: float):
    print(x, "\n")

def performCalcLoop(calc):
    while True:
        choice = input("Operation? ")
        if choice == 'q':
            break
        elif choice == 'add':
            try:
                a, b = getTwoNumbers()
                displayResult(calc.add(a, b))
            except ValueError as e:
                print(f"Error: {e}")
        elif choice == 'sub':
            try:
                a, b = getTwoNumbers()
                displayResult(calc.sub(a, b))
            except ValueError as e:
                print(f"Error: {e}")
        elif choice == 'divide':
            try:
                a, b = getTwoNumbers()
                displayResult(calc.divide(a, b))
            except ValueError as e:
                print(f"Error: {e}")
        elif choice == 'sqrt':
            try:
                a = getOneNumber()
                displayResult(calc.sqrt(a))
            except ValueError as e:
                print(f"Error: {e}")
        elif choice == 'square':
            try:
                a = getOneNumber()
                displayResult(calc.square(a))
            except ValueError as e:
                print(f"Error: {e}")
        elif choice == 'exponent':
            try:
                a, b = getTwoNumbers()
                displayResult(calc.exponent(a, b))
            except ValueError as e:
                print(f"Error: {e}")
        elif choice == 'inverse':
            try:
                a = getOneNumber()
                displayResult(calc.inverse(a))
            except ValueError as e:
                print(f"Error: {e}")
        elif choice == 'switchsign':
            try:
                a = getOneNumber()
                displayResult(calc.switchsign(a))
            except ValueError as e:
                print(f"Error: {e}")
        else:
            print("That is not a valid input.")

# main start
def main():
    calc = Calculator()
    performCalcLoop(calc)
    print("Done Calculating.")

if __name__ == '__main__':
    main()
