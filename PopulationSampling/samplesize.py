from src.Operations.square import Square
from src.DescriptiveStatistics.zscore import Zscore
from PopulationSampling.marginoferror import MarginOfError
from src.DescriptiveStatistics.std import Std

class Samplesize:

    @staticmethod
    def samplesize(seed, data):
        z = Zscore.zscore(seed, data)
        m = MarginOfError.marginoferror(seed, data)
        std = Std.std(data)
        value = (z * std) / m
        ssz = Square.square(value, 2)
        return ssz
