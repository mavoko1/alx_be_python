import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Create a calculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test addition method with various cases."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)
        self.assertEqual(self.calc.add(-5, -7), -12)
        self.assertEqual(self.calc.add(1.5, 2.5), 4.0)

    def test_subtraction(self):
        """Test subtraction method with various cases."""
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(0, 5), -5)
        self.assertEqual(self.calc.subtract(-5, -5), 0)
        self.assertEqual(self.calc.subtract(10, 20), -10)
        self.assertEqual(self.calc.subtract(2.5, 1.0), 1.5)

    def test_multiplication(self):
        """Test multiplication method with various cases."""
        self.assertEqual(self.calc.multiply(4, 5), 20)
        self.assertEqual(self.calc.multiply(-1, 5), -5)
        self.assertEqual(self.calc.multiply(0, 10), 0)
        self.assertEqual(self.calc.multiply(-3, -6), 18)
        self.assertEqual(self.calc.multiply(2.5, 2), 5.0)

    def test_division(self):
        """Test division method with normal and edge cases."""
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(5, 2), 2.5)
        self.assertEqual(self.calc.divide(-6, -2), 3)
        self.assertEqual(self.calc.divide(0, 5), 0)
        self.assertIsNone(self.calc.divide(5, 0))  # division by zero

if __name__ == '__main__':
    unittest.main()
