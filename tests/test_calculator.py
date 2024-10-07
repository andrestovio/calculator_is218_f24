#pylint: disable=redefined-outer-name
'''Calculator paramertized tests'''
import pytest
from app.calculator import Calculator  # Assuming the class is in a file named calculator.py

#Fixture to create a Calculator instance for each test
@pytest.fixture
def calculator():
    '''create an instance of calculator'''
    return Calculator.create()

@pytest.mark.parametrize("a, b, expected", [
    (10, 5, 15),
    (1, 1, 2),
    (-1, -1, -2),
    (0, 0, 0),
])
def test_add(calculator, a, b, expected):
    '''test if the addition function works'''
    assert calculator.add(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (10, 5, 5),
    (1, 1, 0),
    (-1, -1, 0),
    (0, 0, 0),
])
def test_subtract(calculator, a, b, expected):
    '''test if the subtraction function works'''
    assert calculator.subtract(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (10, 5, 50),
    (1, 1, 1),
    (-1, -1, 1),
    (0, 10, 0),
])
def test_multiply(calculator, a, b, expected):
    '''test if the multiplication function works'''
    assert calculator.multiply(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (10, 5, 2),
    (1, 1, 1),
    (-10, -2, 5),
    (0, 1, 0),
])
def test_divide(calculator, a, b, expected):
    '''test if the division function works'''
    assert calculator.divide(a, b) == expected

#Test for division by zero
def test_divide_by_zero(calculator):
    '''test if the divide by zero error is properly displayed'''
    assert calculator.divide(10, 0) == "Error: Division by zero!"