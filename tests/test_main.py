#pylint: disable = redefined-outer-name
'''Parametrized tests for calculator'''
from unittest.mock import patch
import pytest
from main import repl

@pytest.fixture
def inputs_and_expected_outputs():
    '''Fixture for simulating the REPL inputs and outputs'''
    return [
        ("add 10 5\n", "Result: 15.0"),           # Add two numbers
        ("sub 10 5\n", "Result: 5.0"),            # Subtract two numbers
        ("mul 3 4\n", "Result: 12.0"),            # Multiply two numbers
        ("div 10 2\n", "Result: 5.0"),            # Divide two numbers
        ("div 10 0\n", "Error: Division by zero!"),  # Division by zero
    ]

#Parameterized test for each input-output pair
@pytest.mark.parametrize("user_input, expected_output", [
    ("add 10 5\n", "Result: 15.0"),
    ("sub 10 5\n", "Result: 5.0"),
    ("mul 3 4\n", "Result: 12.0"),
    ("div 10 2\n", "Result: 5.0"),
    ("div 10 0\n", "Error: Division by zero!"),
])
def test_repl_integration(user_input, expected_output, capsys):
    '''Patch the input() to simulate user command and end with exit'''
    with patch("builtins.input", side_effect=[user_input, "exit\n"]):
        repl()  # Call the REPL function

    # Capture the output printed by REPL
    captured = capsys.readouterr().out

    # Validate that the expected result is part of the printed output
    assert expected_output in captured

#Test to check REPL flow with multiple commands in sequence
def test_repl_integration_with_sequence(inputs_and_expected_outputs, capsys):
    '''Get inputs and expected outputs from fixture'''
    inputs, expected_outputs = zip(*inputs_and_expected_outputs)

    # Append "exit" at the end to simulate quitting the REPL
    inputs = list(inputs) + ["exit\n"]

    # Patch the input() to simulate the full sequence of commands
    with patch("builtins.input", side_effect=inputs):
        repl()  # Call the REPL function

    # Capture the output printed by REPL
    captured = capsys.readouterr().out

    # Validate each expected output in the captured output
    for expected in expected_outputs:
        assert expected in captured

    # Validate that the REPL ended with the exit message
    assert "Exiting calculator. Goodbye!" in captured
    