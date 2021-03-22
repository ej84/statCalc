import random


class SimpleRandom:

    @staticmethod
    def random_sampling(seq, k):
        return random.sample(seq, k)
