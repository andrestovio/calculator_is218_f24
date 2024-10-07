#main.py

from app.calculator import Calculator

class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            return "Error: Division by zero!"

def display_menu():
    print("\nSimple Calculator")
    print("Available commands:")
    print("add [a] [b] - Adds two numbers")
    print("sub [a] [b] - Subtracts second number from first")
    print("mul [a] [b] - Multiplies two numbers")
    print("div [a] [b] - Divides first number by second")
    print("exit - Exit the calculator")

def parse_input(input_str):
    tokens = input_str.strip().split()
    if len(tokens) < 3 and tokens[0] != 'exit':
        print("Invalid input. Please enter a valid command.")
        return None, None, None
    command = tokens[0]
    if command != 'exit':
        try:
            a = float(tokens[1])
            b = float(tokens[2])
        except ValueError:
            print("Invalid numbers. Please enter numeric values.")
            return None, None, None
        return command, a, b
    return command, None, None

def repl():
    # Create an instance of Calculator
    calc = Calculator()

    display_menu()

    while True:
        userinput = input("\nEnter command: ")
        command, a, b = parse_input(userinput)

        if command == 'exit':
            print("Exiting calculator. Goodbye!")
            break

        if command == 'add':
            print(f"Result: {calc.add(a, b)}")
        elif command == 'sub':
            print(f"Result: {calc.subtract(a, b)}")
        elif command == 'mul':
            print(f"Result: {calc.multiply(a, b)}")
        elif command == 'div':
            print(f"Result: {calc.divide(a, b)}")
        else:
            print("Unknown command. Please try again.")

if __name__ == "__main":
    repl()
    