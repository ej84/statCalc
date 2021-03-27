import unittest
from src.Operations.add import Add
from src.Operations.subtract import Subtract
from src.Operations.multiply import Multiply
from src.Operations.divide import Divide
from src.Operations.square import Square
from src.Operations.root import Root
from src.Operations.log import Log


class OperationsTestCase(unittest.TestCase):

    def test_add(self):
        self.assertEqual(Add.add(5, 7), 12)

    def test_subtract(self):
        self.assertEqual(Subtract.subtract(20, 5), 15)

    def test_multiply(self):
        self.assertEqual(Multiply.multiply(10, 100), 1000)

    def test_divide(self):
        self.assertEqual(Divide.divide(7, 49), 7)

    def test_square(self):
        self.assertEqual(Square.square(11, 2), 121)

    def test_root(self):
        self.assertEqual(Root.root(121), 11)

    def test_log(self):
        self.assertEqual(Log.log(25, 100), 1.4306765580733933)


if __name__ == '__main__':
    unittest.main()
