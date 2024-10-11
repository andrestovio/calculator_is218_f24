# calculator.py

from abc import ABC, abstractmethod

# Strategy Interface (Abstract class for mathematical operations)
class OperationStrategy(ABC):
    @abstractmethod
    def execute(self, a, b):
        pass

# Concrete Strategy for Addition
class AddStrategy(OperationStrategy):
    def execute(self, a, b):
        return a + b

# Concrete Strategy for Subtraction
class SubtractStrategy(OperationStrategy):
    def execute(self, a, b):
        return a - b

# Concrete Strategy for Multiplication
class MultiplyStrategy(OperationStrategy):
    def execute(self, a, b):
        return a * b

# Concrete Strategy for Division
class DivideStrategy(OperationStrategy):
    def execute(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            return "Error: Division by zero!"

# Factory to create the correct strategy based on command
class OperationFactory:
    @staticmethod
    def get_strategy(command):
        if command == 'add':
            return AddStrategy()
        elif command == 'sub':
            return SubtractStrategy()
        elif command == 'mul':
            return MultiplyStrategy()
        elif command == 'div':
            return DivideStrategy()
        else:
            return None

# Calculator class responsible for executing strategies
class Calculator:
    def __init__(self):
        self.strategy = None

    # Set strategy dynamically based on user input
    def set_strategy(self, strategy):
        self.strategy = strategy

    # Execute the current strategy with given numbers
    def calculate(self, a, b):
        if self.strategy:
            return self.strategy.execute(a, b)
        else:
            return "Unknown command. Please try again."

# User interface and command parsing logic
def display_menu():
    """Displays available commands for the calculator."""
    print("\nSimple Calculator")
    print("Available commands:")
    print("add [a] [b] - Adds two numbers")
    print("sub [a] [b] - Subtracts second number from first")
    print("mul [a] [b] - Multiplies two numbers")
    print("div [a] [b] - Divides first number by second")
    print("exit - Exit the calculator")

def parse_input(input_str):
    """Parses the user's input and returns command and two numbers."""
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
    """Read-Evaluate-Print Loop that runs the calculator."""
    calc = Calculator()
    display_menu()

    while True:
        userinput = input("\nEnter command: ")
        command, a, b = parse_input(userinput)

        if command == 'exit':
            print("Exiting calculator. Goodbye!")
            break

        # Get the correct strategy based on user command
        strategy = OperationFactory.get_strategy(command)

        # If strategy exists, set it and calculate the result
        if strategy:
            calc.set_strategy(strategy)
            print(f"Result: {calc.calculate(a, b)}")
        else:
            print("Unknown command. Please try again.")

if __name__ == '__main__':
    repl()
