#!/usr/bin/env python
# coding: utf-8
"""
Simple calculator class for basic arithmetic operations.

Author: Fabrice JUMEL
"""
from typing import Union


class SimpleCalculator:
    """Calculatrice simple (+, -, *, /) avec validation entrées."""

    def fsum(self, int_a: int, int_b: int) -> int:
        """Additionne deux entiers.

        Args:
            int_a: Premier entier.
            int_b: Deuxième entier.

        Returns:
            Somme des deux entiers.
        
        Raises:
            TypeError: Si paramètres non entiers.
        
        Examples:
            >>> calc = SimpleCalculator()
            >>> calc.fsum(2, 3)
            5
            >>> calc.fsum(2.5, 3)
            Traceback: TypeError: Parameters must be integers
        """
        if not isinstance(int_a, int) or not isinstance(int_b, int):
            raise TypeError(f"Parameters must be integers, got {type(int_a).__name__}, {type(int_b).__name__}")
        return int_a + int_b

    def substract(self, int_a: int, int_b: int) -> int:
        """Soustrait int_b de int_a.

        Raises:
            TypeError: Si paramètres non entiers.
        """
        if not isinstance(int_a, int) or not isinstance(int_b, int):
            raise TypeError(f"Parameters must be integers, got {type(int_a).__name__}, {type(int_b).__name__}")
        return int_a - int_b

    def multiply(self, int_a: int, int_b: int) -> int:
        """Multiplie deux entiers.

        Raises:
            TypeError: Si paramètres non entiers.
        """
        if not isinstance(int_a, int) or not isinstance(int_b, int):
            raise TypeError(f"Parameters must be integers, got {type(int_a).__name__}, {type(int_b).__name__}")
        return int_a * int_b

    def divide(self, int_a: int, int_b: int) -> float:
        """Divise int_a par int_b.

        Raises:
            TypeError: Si paramètres non entiers.
            ZeroDivisionError: Si int_b == 0.
        """
        if not isinstance(int_a, int) or not isinstance(int_b, int):
            raise TypeError(f"Parameters must be integers, got {type(int_a).__name__}, {type(int_b).__name__}")
        if int_b == 0:
            raise ZeroDivisionError("Division par zéro impossible")
        return int_a / int_b

