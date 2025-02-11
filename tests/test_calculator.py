"""
Unit tests for the Calculator class.
"""

import pytest
from calculator.calculator import Calculator

def test_add():
    """Test addition operation."""
    assert Calculator.add(5, 3) == 8
    assert Calculator.add(-1, 1) == 0
    assert Calculator.add(0, 0) == 0

def test_subtract():
    """Test subtraction operation."""
    assert Calculator.subtract(5, 3) == 2
    assert Calculator.subtract(1, 1) == 0
    assert Calculator.subtract(0, 5) == -5

def test_multiply():
    """Test multiplication operation."""
    assert Calculator.multiply(5, 3) == 15
    assert Calculator.multiply(-1, 1) == -1
    assert Calculator.multiply(0, 5) == 0

def test_divide():
    """Test division operation."""
    assert Calculator.divide(6, 3) == 2
    assert Calculator.divide(-9, 3) == -3
    assert Calculator.divide(10, 2) == 5

def test_divide_by_zero():
    """Test division by zero raises an exception."""
    with pytest.raises(ZeroDivisionError):
        Calculator.divide(5, 0)
