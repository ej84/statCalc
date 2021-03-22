import unittest
from src.Calculator import Calculator


class CalculatorTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_sum(self):
        self.assertEqual(self.calculator.sum(3, 4), 7)

    def test_difference(self):
        


if __name__ == '__main__':
    unittest.main()
