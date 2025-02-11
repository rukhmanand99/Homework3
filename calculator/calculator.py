"""
Intermediate Calculator with calculation history.
"""

from typing import List
from calculator.calculation import Calculation

class Calculator:
    """A calculator that supports arithmetic operations and stores history."""

    history: List[Calculation] = []

    @staticmethod
    def add(a: float, b: float) -> float:
        """Performs addition and stores in history."""
        calc = Calculation(lambda x, y: x + y, a, b)
        Calculator.history.append(calc)
        return calc.get_result()

    @staticmethod
    def subtract(a: float, b: float) -> float:
        """Performs subtraction and stores in history."""
        calc = Calculation(lambda x, y: x - y, a, b)
        Calculator.history.append(calc)
        return calc.get_result()

    @staticmethod
    def multiply(a: float, b: float) -> float:
        """Performs multiplication and stores in history."""
        calc = Calculation(lambda x, y: x * y, a, b)
        Calculator.history.append(calc)
        return calc.get_result()

    @staticmethod
    def divide(a: float, b: float) -> float:
        """Performs division and stores in history. Raises an error if dividing by zero."""
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        calc = Calculation(lambda x, y: x / y, a, b)
        Calculator.history.append(calc)
        return calc.get_result()

    @classmethod
    def get_history(cls) -> List[Calculation]:
        """Returns the list of past calculations."""
        return cls.history

    @classmethod
    def clear_history(cls):
        """Clears all stored calculations."""
        cls.history.clear()
