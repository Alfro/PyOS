# PyOS
# Made for Python 2.7
# programs/calculator.py

# Import Libraries
# PyOS Scripts
import internal.extra
import internal.runCommand

# Variables

appName = ("Calculator")
validModes = (["a", "s", "m", "d"])

class modulo:

    @staticmethod
    def add(x, y):
        return (x + y)

    @staticmethod
    def subtract(x, y):
        return (x - y)

    @staticmethod
    def multiply(x, y):
        return (x * y)

    @staticmethod
    def divide(x, y):
        return (x / y)

def app():
    internal.runCommand.commands.clear()
    print(internal.extra.colors.BOLD + internal.extra.notes.name + " " + appName + internal.extra.colors.ENDC)
    modeSelect()

def modeSelect():
    print(internal.extra.colors.OKGREEN + "Choose a mode" + internal.extra.colors.ENDC)
    print(internal.extra.colors.OKBLUE + "(A)dd - (S)ubtract - (M)ultiply - (D)ivide - (E)xit" + internal.extra.colors.ENDC)
    choice = raw_input("Mode > ").lower()
    if choice in validModes:
        number1 = raw_input("First Number > ")
        number2 = raw_input("Second Number > ")
        print(calculate(choice, number1, number2))
        modeSelect()
    else:
            if choice == "e":
                return
            modeSelect()

def calculate(mode, number1, number2):
    if (mode == "a"):
        return number1 + " + " + number2 + " = " + str(modulo.add(float(number1), float(number2)))

    if (mode == "s"):
        return number1 + " - " + number2 + " = " + str(modulo.subtract(float(number1), float(number2)))

    if (mode == "m"):
        return number1 + " * " + number2 + " = " + str(modulo.multiply(float(number1), float(number2)))

    if (mode == "d"):
        return number1 + " / " + number2 + " = " + str(modulo.divide(float(number1), float(number2)))
