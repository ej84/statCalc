import unittest
import numpy as np
import scipy.stats

from PopulationSampling.confidence import Confidence
from PopulationSampling.marginoferror import MarginOfError
from PopulationSampling.samplesize import Samplesize
from PopulationSampling.simpleRandom import SimpleRandom


class PopulationTestCase(unittest.TestCase):

    def test_confidence_interval(self):
        sample_list = [1, 2, 3, 4, 5]
        c = 0.95
        df = len(sample_list) - 1
        sample_mean = np.mean(sample_list)
        sample_standard_err = scipy.stats.sem(sample_list)
        ci = Confidence.confidence_interval(c, df, sample_mean, sample_standard_err)
        self.assertEqual(ci, Confidence.confidence_interval(c, df, sample_mean, sample_standard_err))


    def test_marinoferror(self):
        sample_list = [1.11, 2.34, 3.91, 4.22, 5.12]
        me = MarginOfError.marginoferror(sample_list)
        self.assertEqual(me.all(), MarginOfError.marginoferror(sample_list).all())


if __name__ == '__main__':
    unittest.main()
