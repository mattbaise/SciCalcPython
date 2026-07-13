from calculator import Calculator


def getTwoNumbers():
    a = float(input("first number? "))
    b = float(input("second number? "))
    return a, b

# Easter Egg Check
def check_easter_egg(operation):
    if operation == 2813308004:
        print("WHO?? MIKE JONES!!")

def displayResult(x: float):
    print(x, "\n")


def toggle_mode(current_mode: str) -> str:
    return "scientific" if current_mode == "basic" else "basic"


def set_mode(current_mode: str, requested_mode: str) -> str:
    if requested_mode in {"basic", "scientific"}:
        return requested_mode
    return current_mode


def current_mode_label(mode_name: str) -> str:
    if mode_name == "basic":
        return "Basic Calculator Mode"
    return "Scientific Calculator Mode"


def angle_mode_label(angle_mode: str) -> str:
    return "Degrees" if angle_mode == "degrees" else "Radians"


def degree_to_radian(degree: float) -> float:
    return degree * (3.14159 / 180.0)

def radian_to_degree(radian: float) -> float:
    return radian * (180.0 / 3.14159)

def normalize_operation(choice: str) -> str:
    normalized = choice.strip().lower()
    normalized = normalized.replace("-", " ").replace("_", " ")
    normalized = " ".join(normalized.split())

    aliases = {
        "+": "add",
        "-": "sub",
        "*": "multiply",
        "/": "division",
        "^": "variableExponent",
        "sqrt": "squareRoot",
        "square root": "squareRoot",
        "square": "square",
        "sin": "sin",
        "cos": "cos",
        "tan": "tan",
        "asin": "inverseSin",
        "acos": "inverseCos",
        "atan": "inverseTan",
        "inverse sin": "inverseSin",
        "inverse cos": "inverseCos",
        "inverse tan": "inverseTan",
        "variable exponent": "variableExponent",
        "degreetoradian": "degreeToRadian",
        "radian to degree": "radianToDegree",
        "radian todegree": "radianToDegree",
        "degree to radian": "degreeToRadian",
        "degree toradian": "degreeToRadian",
    }

    if normalized in aliases:
        return aliases[normalized]

    if normalized in {"inversesin", "inversesin"}:
        return "inverseSin"
    if normalized in {"inversecos", "inversecos"}:
        return "inverseCos"
    if normalized in {"inversetan", "inversetan"}:
        return "inverseTan"
    if normalized in {"squareroot", "square root"}:
        return "squareRoot"
    if normalized in {"degreetoradian", "degree to radian", "degree toradian"}:
        return "degreeToRadian"
    if normalized in {"radiantodegree", "radian to degree", "radian todegree"}:
        return "radianToDegree"

    return normalized


def performCalcLoop(calc):
    mode_name = "basic"

    while True:
        print(current_mode_label(mode_name))
        choice = input("Operation? ")
        operation = normalize_operation(choice)

        if operation == 'q':
            break
        elif operation in {"basic", "scientific"}:
            mode_name = set_mode(mode_name, operation)
            print(current_mode_label(mode_name))
        elif operation == 'toggle':
            mode_name = toggle_mode(mode_name)
            print(current_mode_label(mode_name))
        elif mode_name == 'basic' and operation == 'add':
            a, b = getTwoNumbers()
            check_easter_egg(a)
            check_easter_egg(b)
            displayResult(calc.add(a, b))
        elif mode_name == 'basic' and operation == 'sub':
            a, b = getTwoNumbers()
            check_easter_egg(a)
            check_easter_egg(b)
            displayResult(calc.sub(a, b))
        elif mode_name == 'basic' and operation == 'multiply':
            a, b = getTwoNumbers()
            check_easter_egg(a)
            check_easter_egg(b)
            displayResult(calc.multiply(a, b))
        elif mode_name == 'basic' and operation == 'division':
            a, b = getTwoNumbers()
            check_easter_egg(a)
            check_easter_egg(b)
            displayResult(calc.division(a, b))
        elif mode_name == 'scientific' and operation == 'add':
            a, b = getTwoNumbers()
            check_easter_egg(a)
            check_easter_egg(b)
            displayResult(calc.add(a, b))
        elif mode_name == 'scientific' and operation == 'sub':
            a, b = getTwoNumbers()
            check_easter_egg(a)
            check_easter_egg(b)
            displayResult(calc.sub(a, b))
        elif mode_name == 'scientific' and operation == 'multiply':
            a, b = getTwoNumbers()
            check_easter_egg(a)
            check_easter_egg(b)
            displayResult(calc.multiply(a, b))
        elif mode_name == 'scientific' and operation == 'division':
            a, b = getTwoNumbers()
            check_easter_egg(a)
            check_easter_egg(b)
            displayResult(calc.division(a, b))
        elif mode_name == 'scientific' and operation == 'square':
            a = float(input("number? "))
            check_easter_egg(a)
            displayResult(calc.square(a))
        elif mode_name == 'scientific' and operation == 'squareRoot':
            a = float(input("number? "))
            check_easter_egg(a)
            displayResult(calc.squareRoot(a))
        elif mode_name == 'scientific' and operation == 'variableExponent':
            a, b = getTwoNumbers()
            check_easter_egg(a)
            check_easter_egg(b)
            displayResult(calc.variableExponent(a, b))
        elif mode_name == 'scientific' and operation == 'sin':
            a = float(input("number? "))
            check_easter_egg(a)
            displayResult(calc.sin(a))
        elif mode_name == 'scientific' and operation == 'cos':
            a = float(input("number? "))
            check_easter_egg(a)
            displayResult(calc.cos(a))
        elif mode_name == 'scientific' and operation == 'tan':
            a = float(input("number? "))
            check_easter_egg(a)
            displayResult(calc.tan(a))
        elif mode_name == 'scientific' and operation == 'inverseSin':
            a = float(input("number? "))
            check_easter_egg(a)
            displayResult(calc.inverseSin(a))
        elif mode_name == 'scientific' and operation == 'inverseCos':
            a = float(input("number? "))
            check_easter_egg(a)
            displayResult(calc.inverseCos(a))
        elif mode_name == 'scientific' and operation == 'inverseTan':
            a = float(input("number? "))
            check_easter_egg(a)
            displayResult(calc.inverseTan(a))
        elif mode_name == 'scientific' and operation == 'factorial':
            a = float(input("number? "))
            check_easter_egg(a)
            displayResult(calc.factorial(a))
        elif mode_name == 'scientific' and operation == 'degreeToRadian':
            a = float(input("degree? "))
            check_easter_egg(a)
            displayResult(degree_to_radian(a))
        elif mode_name == 'scientific' and operation == 'radianToDegree':
            a = float(input("radian? "))
            check_easter_egg(a)
            displayResult(radian_to_degree(a))
        else:
            print("That is not a valid input.")



# main start
def main():
    calc = Calculator()
    performCalcLoop(calc)
    print("Done Calculating.")


if __name__ == '__main__':
    main()
