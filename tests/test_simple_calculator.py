"""Tests unitaires pour SimpleCalculator.

Author: Fabrice JUMEL
"""
import unittest
from calculator import SimpleCalculator


class TestSimpleCalculator(unittest.TestCase):
    """Tests calculatrice simple avec exceptions."""

    def setUp(self):
        """Initialise calculatrice avant chaque test."""
        self.calc = SimpleCalculator()

    # ========== Tests fsum ==========
    def test_fsum_valid_positive(self):
        """Test addition entiers positifs."""
        self.assertEqual(self.calc.fsum(2, 3), 5)
        self.assertEqual(self.calc.fsum(10, 20), 30)
        self.assertEqual(self.calc.fsum(100, 200), 300)

    def test_fsum_valid_negative(self):
        """Test addition avec négatifs."""
        self.assertEqual(self.calc.fsum(-1, 1), 0)
        self.assertEqual(self.calc.fsum(-5, -3), -8)
        self.assertEqual(self.calc.fsum(-10, 20), 10)

    def test_fsum_valid_zero(self):
        """Test addition avec zéro."""
        self.assertEqual(self.calc.fsum(0, 0), 0)
        self.assertEqual(self.calc.fsum(5, 0), 5)
        self.assertEqual(self.calc.fsum(0, 5), 5)

    def test_fsum_invalid_float(self):
        """Test addition float lève TypeError."""
        with self.assertRaises(TypeError):
            self.calc.fsum(2.5, 3)
        with self.assertRaises(TypeError):
            self.calc.fsum(2, 3.5)
        with self.assertRaises(TypeError):
            self.calc.fsum(2.5, 3.5)

    def test_fsum_invalid_string(self):
        """Test addition string lève TypeError."""
        with self.assertRaises(TypeError):
            self.calc.fsum("2", 3)
        with self.assertRaises(TypeError):
            self.calc.fsum(2, "3")
        with self.assertRaises(TypeError):
            self.calc.fsum("a", "b")

    def test_fsum_invalid_none(self):
        """Test addition None lève TypeError."""
        with self.assertRaises(TypeError):
            self.calc.fsum(None, 3)
        with self.assertRaises(TypeError):
            self.calc.fsum(2, None)

    def test_fsum_invalid_bool(self):
        """Test addition bool lève TypeError (edge case)."""
        # Note: isinstance(True, int) == True en Python
        # Si tu veux rejeter bools, ajoute check explicite
        # Sinon True=1, False=0
        result = self.calc.fsum(True, False)
        self.assertEqual(result, 1)  # True=1, False=0

    # ========== Tests substract ==========
    def test_substract_valid_positive(self):
        """Test soustraction entiers positifs."""
        self.assertEqual(self.calc.substract(5, 3), 2)
        self.assertEqual(self.calc.substract(10, 5), 5)
        self.assertEqual(self.calc.substract(100, 50), 50)

    def test_substract_valid_negative(self):
        """Test soustraction avec négatifs."""
        self.assertEqual(self.calc.substract(-5, -3), -2)
        self.assertEqual(self.calc.substract(5, -3), 8)
        self.assertEqual(self.calc.substract(-5, 3), -8)

    def test_substract_valid_zero(self):
        """Test soustraction avec zéro."""
        self.assertEqual(self.calc.substract(0, 0), 0)
        self.assertEqual(self.calc.substract(5, 0), 5)
        self.assertEqual(self.calc.substract(0, 5), -5)

    def test_substract_invalid_types(self):
        """Test soustraction types invalides."""
        with self.assertRaises(TypeError):
            self.calc.substract(5.5, 3)
        with self.assertRaises(TypeError):
            self.calc.substract("5", 3)

    # ========== Tests multiply ==========
    def test_multiply_valid_positive(self):
        """Test multiplication entiers positifs."""
        self.assertEqual(self.calc.multiply(4, 3), 12)
        self.assertEqual(self.calc.multiply(10, 5), 50)
        self.assertEqual(self.calc.multiply(7, 6), 42)

    def test_multiply_valid_negative(self):
        """Test multiplication avec négatifs."""
        self.assertEqual(self.calc.multiply(-4, 3), -12)
        self.assertEqual(self.calc.multiply(-4, -3), 12)
        self.assertEqual(self.calc.multiply(4, -3), -12)

    def test_multiply_valid_zero(self):
        """Test multiplication par zéro."""
        self.assertEqual(self.calc.multiply(0, 0), 0)
        self.assertEqual(self.calc.multiply(5, 0), 0)
        self.assertEqual(self.calc.multiply(0, 5), 0)

    def test_multiply_valid_one(self):
        """Test multiplication par un."""
        self.assertEqual(self.calc.multiply(1, 1), 1)
        self.assertEqual(self.calc.multiply(5, 1), 5)
        self.assertEqual(self.calc.multiply(1, 5), 5)

    def test_multiply_invalid_types(self):
        """Test multiplication types invalides."""
        with self.assertRaises(TypeError):
            self.calc.multiply(4.5, 3)
        with self.assertRaises(TypeError):
            self.calc.multiply("4", 3)

    # ========== Tests divide ==========
    def test_divide_valid_positive(self):
        """Test division entiers positifs."""
        self.assertEqual(self.calc.divide(10, 2), 5.0)
        self.assertEqual(self.calc.divide(15, 3), 5.0)
        self.assertEqual(self.calc.divide(100, 4), 25.0)

    def test_divide_valid_result_float(self):
        """Test division résultat float."""
        self.assertEqual(self.calc.divide(10, 3), 10/3)
        self.assertEqual(self.calc.divide(7, 2), 3.5)
        self.assertAlmostEqual(self.calc.divide(1, 3), 0.333333, places=5)

    def test_divide_valid_negative(self):
        """Test division avec négatifs."""
        self.assertEqual(self.calc.divide(-10, 2), -5.0)
        self.assertEqual(self.calc.divide(10, -2), -5.0)
        self.assertEqual(self.calc.divide(-10, -2), 5.0)

    def test_divide_valid_by_one(self):
        """Test division par un."""
        self.assertEqual(self.calc.divide(5, 1), 5.0)
        self.assertEqual(self.calc.divide(-5, 1), -5.0)

    def test_divide_zero_denominator(self):
        """Test division par zéro lève ZeroDivisionError."""
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(10, 0)
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(0, 0)
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(-10, 0)

    def test_divide_zero_numerator(self):
        """Test division zéro par nombre."""
        self.assertEqual(self.calc.divide(0, 5), 0.0)
        self.assertEqual(self.calc.divide(0, -5), 0.0)

    def test_divide_invalid_float(self):
        """Test division float lève TypeError."""
        with self.assertRaises(TypeError):
            self.calc.divide(10.5, 2)
        with self.assertRaises(TypeError):
            self.calc.divide(10, 2.5)

    def test_divide_invalid_string(self):
        """Test division string lève TypeError."""
        with self.assertRaises(TypeError):
            self.calc.divide("10", 2)
        with self.assertRaises(TypeError):
            self.calc.divide(10, "2")

    # ========== Tests Edge Cases ==========
    def test_large_numbers(self):
        """Test grandes valeurs."""
        self.assertEqual(self.calc.fsum(999999, 1), 1000000)
        self.assertEqual(self.calc.multiply(1000, 1000), 1000000)
        self.assertEqual(self.calc.divide(1000000, 1000), 1000.0)

    def test_type_consistency(self):
        """Test cohérence types retour."""
        # fsum, substract, multiply retournent int
        self.assertIsInstance(self.calc.fsum(2, 3), int)
        self.assertIsInstance(self.calc.substract(5, 3), int)
        self.assertIsInstance(self.calc.multiply(4, 3), int)
        
        # divide retourne float
        self.assertIsInstance(self.calc.divide(10, 2), float)


if __name__ == '__main__':
    unittest.main(verbosity=2)
