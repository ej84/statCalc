import scipy.stats as st


class Confidence:
    # c_level = confidence level, df = degrees freedom, sample_std_error: sample standard error
    @staticmethod
    def confidence_interval(c_level, degrees_freedom, sample_mean, sample_std_err):
        return st.t.interval(c_level, degrees_freedom, sample_mean, sample_std_err)
