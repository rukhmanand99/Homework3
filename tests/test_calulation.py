"""
Unit tests for the Calculations class.
"""

from calculator.calculations import Calculations
from calculator.calculation import Calculation

def setup_function():
    """Clear history before each test."""
    Calculations.clear_history()

def test_add_calculation():
    """Test adding a calculation to history."""
    calc = Calculation(lambda x, y: x + y, 2, 3)
    Calculations.add_calculation(calc)
    assert len(Calculations.get_history()) == 1

def test_clear_history():
    """Test clearing history."""
    Calculations.add_calculation(Calculation(lambda x, y: x + y, 2, 3))
    Calculations.clear_history()
    assert len(Calculations.get_history()) == 0
