from src.DescriptiveStatistics.zscore import Zscore
from src.DescriptiveStatistics.std import Std


class MarginOfError:

    @staticmethod
    def marginoferror(seed, data):
        zscore = Zscore.zscore(seed, data)
        std = Std.std(data)
        return zscore * std
