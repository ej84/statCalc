from src.DescriptiveStatistics.zscore import Zscore
from src.DescriptiveStatistics.std import Std


class MarginOfError:

    @staticmethod
    def marginoferror(data):
        zscore = Zscore.zscore(data)
        std = Std.std(data)
        return zscore * std
