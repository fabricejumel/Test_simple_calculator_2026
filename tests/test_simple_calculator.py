import unittest
from calculator import SimpleCalculator


class TestSimpleCalculator(unittest.TestCase):
    """Tests calculatrice simple."""

    def setUp(self):
        """Initialise calculatrice avant chaque test."""
        self.calc = SimpleCalculator("config.toml")

    def test_fsum_valid(self):
        """Test addition entiers valides."""
        self.assertEqual(self.calc.fsum(2, 3), 5)
        self.assertEqual(self.calc.fsum(-1, 1), 0)

    def test_fsum_invalid(self):
        """Test addition types invalides."""
        self.assertEqual(self.calc.fsum(2.5, 3), "ERROR")
        self.assertEqual(self.calc.fsum("2", 3), "ERROR")

    def test_substract_valid(self):
        """Test soustraction."""
        self.assertEqual(self.calc.substract(5, 3), 2)

    def test_multiply_valid(self):
        """Test multiplication."""
        self.assertEqual(self.calc.multiply(4, 3), 12)

    def test_divide_valid(self):
        """Test division valide."""
        self.assertEqual(self.calc.divide(10, 2), 5.0)

    def test_divide_zero(self):
        """Test division par zéro lève exception."""
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(10, 0)

    def test_divide_invalid_type(self):
        """Test division type invalide."""
        self.assertEqual(self.calc.divide(10.0, 2), "ERROR")


if __name__ == '__main__':
    unittest.main()
