from calculator import Calculator
import tkinter as tk
from tkinter import ttk


root = tk.Tk() #this is the main window of the calculator. It is created using the Tk() function from the tkinter module. The root variable is used to reference this window throughout the program.
root.title("Data General Scientific Calculator")
root.geometry("400x400")

display_var = tk.StringVar() #this variable is used to store the current value of the calculator's display. It is set to "0" and is updated whenever the user inputs a number or an operation.
display_var.set("0")  #this variable is used to store the current value of the calculator's display. 
calc_state = 0.0 #this variable is used to store the current state of the calculator. 
angle_mode = tk.StringVar() #this variable is used to store the current angle mode of the calculator. It is set to "DEG" and is updated whenever the user inputs an angle mode.
angle_mode.set("DEG")

memory = 0.0 #this variable is used to store the current value of the calculator's memory. It is set to 0 and is updated whenever the user inputs a number or an operation.


def getTwoNumbers(): #this function gets two numbers from the user and returns them as floats.
    a = float(input("first number? "))
    b = float(input("second number? "))
    return a, b

def getOneNumber(): #this function gets one number from the user and returns it as a float.
    a = float(input("number? "))
    return a

def displayResult(x: float):
    print(x, "\n")

def performCalcLoop(calc):
    while True:
        choice = input("Operation? ")
        if choice == 'q':
            break  # user types q to quit calulator.
        elif choice == 'add':
            a, b = getTwoNumbers()
            displayResult(calc.add(a, b))
        elif choice == 'sub':
            a, b = getTwoNumbers()
            displayResult(calc.sub(a, b))
        elif choice == 'divide':
            a, b = getTwoNumbers()
            displayResult(calc.divide(a, b))
            if b == 0:
                print("Cannot divide by zero.")
        elif choice == 'sqrt':
            a = getOneNumber()
            displayResult(calc.sqrt(a))
            if a < 0:
                print("Cannot take square root of negative number.")
        elif choice == 'square':
            a = getOneNumber()
            displayResult(calc.square(a))
        elif choice == 'exponent':
            a, b = getTwoNumbers()
            displayResult(calc.exponent(a, b))
        elif choice == 'inverse':
            a = getOneNumber()
            displayResult(calc.inverse(a))
            if a == 0:
                    print("Cannot take inverse of zero.")
        elif choice == 'switchsign':
            a = getOneNumber()
            displayResult(calc.switchsign(a))
            if a == 0:
                    print("Cannot switch sign of zero.")

    
        else:
            print("That is not a valid input.")


# main start
def main():
    calc = Calculator()
    performCalcLoop(calc)
    print("Done Calculating.")


if __name__ == '__main__':
    main()
