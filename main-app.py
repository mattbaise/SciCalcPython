from calculator import Calculator
from datetime import datetime

def display_title():
    now= datetime.now()

    print("=" *60)
    print("Welcome Data General's Scientific Calculator")
    print("=" *60)
    print("Current date:", now.strftime("%B %D,%Y"))
    print("Current time:", now.strftime("%H:%M:%S"))
    print("=" *60)

def display_end_title():
    print("=" * 60)
    print("     Thank you for using Data General's")
    print("        Scientific Calculator")
    print()
    print("         Until next time, goodbye!")
    print("=" * 60)


    print("Type 'q' to quit.\n")

def getTwoNumbers():
    a = float(input("first number? "))
    b = float(input("second number? "))
    return a, b

def getOneNumber():
    a = float(input("number? "))
    return a

def displayResult(x: float):
    print(x, "\n")

def runTipCalculator(calc):
    bill = float(input("Bill amount? $"))
    percentage = float(input("Tip percentage? "))
    people = int(input("How many people are splitting the bill? "))
    tip, total, per_person = calc.calculate_tip(bill, percentage, people)
    calc.state = total
    print(f"Tip: ${tip:.2f}")
    print(f"Total: ${total:.2f}")
    print(f"Each person pays: ${per_person:.2f}\n")

def performCalcLoop(calc):
    while True:
        choice = input("Operation? ")
        if choice == 'q':
            break
        elif choice == 'm+':
            calc.M_plus()
            displayResult(calc.state)
        elif choice == 'mc':
            calc.MC()
            print("Memory cleared.\n")
        elif choice == 'mrc':
            displayResult(calc.MRC())
        elif choice == 'tip':
            try:
                runTipCalculator(calc)
            except ValueError as e:
                print(f"Error: {e}")
        elif choice == 'temp':
            try:
                runTemperatureConverter(calc)
            except ValueError as e:
                print(f"Error: {e}")
        elif choice == 'add':
            try:
                a, b = getTwoNumbers()
                calc.state = calc.add(a, b)
                displayResult(calc.state)
            except ValueError as e:
                print(f"Error: {e}")
        elif choice == 'sub':
            try:
                a, b = getTwoNumbers()
                calc.state = calc.sub(a, b)
                displayResult(calc.state)
            except ValueError as e:
                print(f"Error: {e}")
        elif choice == 'divide':
            try:
                a, b = getTwoNumbers()
                calc.state = calc.divide(a, b)
                displayResult(calc.state)
            except ValueError as e:
                print(f"Error: {e}")
        elif choice == 'sqrt':
            try:
                a = getOneNumber()
                calc.state = calc.sqrt(a)
                displayResult(calc.state)
            except ValueError as e:
                print(f"Error: {e}")
        elif choice == 'square':
            try:
                a = getOneNumber()
                calc.state = calc.square(a)
                displayResult(calc.state)
            except ValueError as e:
                print(f"Error: {e}")
        elif choice == 'exponent':
            try:
                a, b = getTwoNumbers()
                calc.state = calc.exponent(a, b)
                displayResult(calc.state)
            except ValueError as e:
                print(f"Error: {e}")
        elif choice == 'inverse':
            try:
                a = getOneNumber()
                calc.state = calc.inverse(a)
                displayResult(calc.state)
            except ValueError as e:
                print(f"Error: {e}")
        elif choice == 'switchsign':
            try:
                a = getOneNumber()
                calc.state = calc.switchsign(a)
                displayResult(calc.state)
            except ValueError as e:
                print(f"Error: {e}")
        else:
            print("That is not a valid input.")

def runTemperatureConverter(calc):
    unit = input("Convert from Fahrenheit or Celsius? (F/C) ").upper()
    temperature = float(input("Temperature? "))
    if unit == "F":
        calc.state = calc.fahrenheit_to_celsius(temperature)
        print(f"{temperature:.2f}°F = {calc.state:.2f}°C\n")
    elif unit == "C":
        calc.state = calc.celsius_to_fahrenheit(temperature)
        print(f"{temperature:.2f}°C = {calc.state:.2f}°F\n")
    else:
        raise ValueError("Please enter F or C.")

# main start
def main():
    display_title()

    calc = Calculator()
    performCalcLoop(calc)

    display_end_title()

    print("Done Calculating.")


if __name__ == '__main__':
    main()
    
