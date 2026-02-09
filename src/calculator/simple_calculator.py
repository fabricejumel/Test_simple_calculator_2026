#!/usr/bin/env python
# coding: utf-8
"""
Simple calculator class for basic arithmetic operations.

Author: Fabrice JUMEL
"""
import tomllib
from typing import Union


class SimpleCalculator:
    """Calculatrice simple (+, -, *, /) avec validation entrées."""

    def __init__(self, config_path: str = "config.toml"):
        """Initialise calculatrice avec config TOML.
        
        Args:
            config_path: Chemin fichier config TOML.
        """
        with open(config_path, 'rb') as f:
            self.cfg = tomllib.load(f).get('calculator', {})
        self.strict_int = self.cfg.get('strict_integers', True)

    def fsum(self, int_a: int, int_b: int) -> Union[int, str]:
        """Additionne deux entiers.

        Args:
            int_a: Premier entier.
            int_b: Deuxième entier.

        Returns:
            Somme des deux entiers ou "ERROR" si types invalides.
        
        Examples:
            >>> calc = SimpleCalculator()
            >>> calc.fsum(2, 3)
            5
        """
        if isinstance(int_a, int) and isinstance(int_b, int):
            return int_a + int_b
        return "ERROR"

    def substract(self, int_a: int, int_b: int) -> Union[int, str]:
        """Soustrait int_b de int_a.

        Args:
            int_a: Entier à soustraire de.
            int_b: Entier à soustraire.

        Returns:
            Différence int_a - int_b ou "ERROR".
        """
        if isinstance(int_a, int) and isinstance(int_b, int):
            return int_a - int_b
        return "ERROR"

    def multiply(self, int_a: int, int_b: int) -> Union[int, str]:
        """Multiplie deux entiers.

        Args:
            int_a: Premier entier.
            int_b: Deuxième entier.

        Returns:
            Produit int_a * int_b ou "ERROR".
        """
        if isinstance(int_a, int) and isinstance(int_b, int):
            return int_a * int_b
        return "ERROR"

    def divide(self, int_a: int, int_b: int) -> Union[float, str]:
        """Divise int_a par int_b.

        Args:
            int_a: Numérateur (entier).
            int_b: Dénominateur (entier non nul).

        Returns:
            Quotient int_a / int_b (float) ou "ERROR".
        
        Raises:
            ZeroDivisionError: Si int_b == 0.
        
        Examples:
            >>> calc.divide(10, 2)
            5.0
        """
        if isinstance(int_a, int) and isinstance(int_b, int):
            if int_b == 0:
                raise ZeroDivisionError("Division par zéro impossible")
            return int_a / int_b
        return "ERROR"
