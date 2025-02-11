"""
Unit tests for the Calculation class.
"""

from calculator.calculation import Calculation

def test_calculation():
    """Test Calculation object creation and result retrieval."""
    calc = Calculation(lambda x, y: x + y, 2, 3)
    assert calc.get_result() == 5
