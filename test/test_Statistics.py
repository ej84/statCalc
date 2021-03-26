import unittest

from src.DescriptiveStatistics.mean import Mean
from src.DescriptiveStatistics.median import Median
from src.DescriptiveStatistics.std import Std
from src.DescriptiveStatistics.mode import Mode
from src.DescriptiveStatistics.zscore import Zscore
from src.DescriptiveStatistics.variance import Variance


class StatsTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.test = [1, 1]
        self.test2 = [1, 3, 5, 7, 9, 11]

    def test_mean(self):
        self.assertEqual(1, Mean.mean(self.test))

    def test_median(self):
        self.assertEqual(6, Median.median(self.test2))

    def test_mode(self):
        self.assertEqual(1, Mode.mode(self.test))

    def test_std(self):
        self.assertEqual(3.7416573867739413, Std.std(self.test2))

    def test_variance(self):
        self.assertEqual(14, Variance.variance(self.test2))

    def test_zscore(self):
        self.zs = Zscore.zscore(self.test2).all()
        self.assertEqual(self.zs, Zscore.zscore(self.test2).all())


if __name__ == '__main__':
    unittest.main()
