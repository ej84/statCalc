import numpy as np
import pandas as pd
import scipy.stats as st

class Zscore:

    @staticmethod
    def zscore(n):
        return st.zscore(n)
