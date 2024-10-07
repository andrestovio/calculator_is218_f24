"File containing the functions for the calculator"
from app.operations import addition, subtraction, multiplication, division


class Calculator:
    '''calculator functions'''

    @staticmethod
    def create():
        '''creates a instance of calculator'''
        return Calculator()

    def add(self, a, b):
        '''adds two numbers together'''
        return addition(a,b)

    def subtract(self, a, b):
        '''subtracts two numbers together'''
        return subtraction(a,b)

    def multiply(self, a, b):
        '''multiplies two numbers together'''
        return multiplication(a,b)

    def divide(self, a, b):
        '''divides two numbers together'''
        if b == 0:
            return "Error: Division by zero!"
        return division(a,b)
