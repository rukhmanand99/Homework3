"""
Unit tests for the Calculator class with parameterized test cases.
"""
# pylint: disable=invalid-name


import pytest
from calculator.calculator import Calculator
from calculator.calculations import Calculations

@pytest.fixture(autouse=True)
def clear_history():
    """Clear calculation history before each test."""
    Calculations.clear_history()

@pytest.mark.parametrize("a, b, expected", [(5, 3, 8), (10, 2, 12), (-1, -1, -2)])
def test_add(a, b, expected):
    """Test addition with different inputs."""
    assert Calculator.add(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [(5, 3, 2), (10, 2, 8), (-1, -1, 0)])
def test_subtract(a, b, expected):
    """Test subtraction with different inputs."""
    assert Calculator.subtract(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [(5, 3, 15), (10, 2, 20), (-1, -1, 1)])
def test_multiply(a, b, expected):
    """Test multiplication with different inputs."""
    assert Calculator.multiply(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [(6, 3, 2), (10, 2, 5), (-4, -2, 2)])
def test_divide(a, b, expected):
    """Test division with different inputs."""
    assert Calculator.divide(a, b) == expected

def test_divide_by_zero():
    """Test division by zero raises an exception."""
    with pytest.raises(ZeroDivisionError):
        Calculator.divide(5, 0)
