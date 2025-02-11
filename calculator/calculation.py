"""
Module for storing individual calculations.
"""

from typing import Callable

class Calculation:
    """Represents a single arithmetic calculation."""

    def __init__(self, operation: Callable[[float, float], float], a: float, b: float):
        """
        Initializes a Calculation instance.

        :param operation: A function representing the arithmetic operation.
        :param a: First operand.
        :param b: Second operand.
        """
        self.operation = operation
        self.a = a
        self.b = b
        self.result = self.operation(self.a, self.b)

    def get_result(self) -> float:
        """Returns the result of the calculation."""
        return self.result
