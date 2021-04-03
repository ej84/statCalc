import unittest

from RandomGenerator.randnums import RandNums
from RandomGenerator.randlist import RandList
from RandomGenerator.listgenerator import ListGenerator

class RandomTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    def test_random_nums(self):
        result = RandNums.randnums(0, 11)
        self.assertEqual(type(result), int)

    def test_random_seed(self):
        result = RandNums.randumseed(11, 0, 20)
        result2 = RandNums.randumseed(11, 0, 20)
        self.assertEqual(type(result) and type(result2), int)
        self.assertEqual(result, result2)
        self.assertEqual(result == result2, True)

    def test_random_float(self):
        result = RandNums.randnumfloat(0, 11)
        self.assertEqual(type(result), float)

    def test_random_float_seed(self):
        result = RandNums.randfloatseed(11, 0, 15)
        result2 = RandNums.randfloatseed(11, 0, 15)
        self.assertEqual(type(result) and type(result2), float)
        self.assertEqual(result, result2)
        self.assertEqual(result == result2, True)

    def test_random_list(self):
        list1 = RandList.randlist(1, 11, 0, 11)
        list2 = RandList.randlist(1, 11, 0, 11)
        self.assertEqual(list1 == list2, True)
        self.assertEqual(type(list1) and type(list2), list)

    def test_random_float_list(self):
        list1 = RandList.randfloatlist(2, 15, 0, 20)
        list2 = RandList.randfloatlist(2, 15, 0, 20)
        self.assertEqual(list1 == list2, True)
        self.assertEqual(type(list1) and type(list2), list)
        self.assertEqual(type(list1[0]) and type(list2[1]), float)

    def test_list_select(self):
        number = ListGenerator.listselect(self.data)
        test_result = None
        if number in self.data and type(number) == int:
            test_result = True
        self.assertEqual(test_result, True)

    def test_list_seed(self):
        num1 = ListGenerator.listseed(5, self.data)
        num2 = ListGenerator.listseed(5, self.data)
        result = None
        if num1 and num2 in self.data and type(num1) and type(num2) == int:
            if num1 == num2:
                result = True
        self.assertEqual(result, True)

    def test_selected_list(self):
        newlist = ListGenerator.listselected(3, self.data)
        result = None
        if len(newlist) == 3:
            for num in newlist:
                if num in self.data and type(num) == int:
                    result = True
        self.assertEqual(result, True)

    def test_selected_seeded_list(self):
        result = None
        result2 = None
        newlist = ListGenerator.listseeded(9, 5, self.data)
        newlist2 = ListGenerator.listseeded(9, 5, self.data)
        if len(newlist) and len(newlist2) == 5:

            for num in newlist:

                if num in self.data and type(num) == int:

                    for num2 in newlist2:

                        if num2 in self.data and type(num2) == int:
                            result = True

                            if newlist == newlist2:
                                result2 = True

        self.assertEqual(result, True)
        self.assertEqual(result2, True)


if __name__ == '__main__':
    unittest.main()
