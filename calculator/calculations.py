"""
Module for managing calculation history.
"""

from typing import List
from calculator.calculation import Calculation

class Calculations:
    """Manages a history of calculations."""

    history: List[Calculation] = []

    @classmethod
    def add_calculation(cls, calculation: Calculation):
        """Adds a calculation to history."""
        cls.history.append(calculation)

    @classmethod
    def get_history(cls) -> List[Calculation]:
        """Returns the history of calculations."""
        return cls.history

    @classmethod
    def clear_history(cls):
        """Clears the calculation history."""
        cls.history.clear()
