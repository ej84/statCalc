import unittest
from src.Calculator.Calculator import Calculator


class CalculatorTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_sum(self):
        self.assertEqual(self.calculator.sum(3, 4), 7)

    def test_difference(self):
        self.assertEqual(self.calculator.difference(1, 4), -3)

    def test_product(self):
        self.assertEqual(self.calculator.product(3, 9), 27)

    def test_quotient(self):
        self.assertEqual(self.calculator.quotient(10, 100), 10)

    def test_power(self):
        self.assertEqual(self.calculator.power(5, 3), 125)

    def test_root(self):
        self.assertEqual(self.calculator.rt(25), 5)


if __name__ == '__main__':
    unittest.main()
