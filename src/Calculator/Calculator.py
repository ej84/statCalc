from src.Operations.add import Add
from src.Operations.subtract import Subtract
from src.Operations.multiply import Multiply
from src.Operations.divide import Divide
from src.Operations.square import Square
from src.Operations.root import Root
from src.Operations.log import Log


class Calculator:

    result = 0

    def __init__(self):
        pass

    def sum(self, a, b):
        self.result = Add.add(a, b)
        return self.result

    def difference(self, a, b):
        self.result = Subtract.subtract(a, b)
        return self.result

    def product(self, a, b):
        self.result = Multiply.multiply(a, b)
        return self.result

    def quotient(self, a, b):
        self.result = Divide.divide(a, b)
        return self.result

    def power(self, a):
        self.result = Square.square(a)
        return self.result

    def rt(self, a):
        self.result = Root.root(a)
        return self.result

    def log(self, a, x):
        self.result = Log.log(a, x)
        return self.result
