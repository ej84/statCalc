import random

class RandNums:

    @staticmethod
    def randnums(minimum, maximum):
        return random.randint(minimum, maximum)

    @staticmethod
    def randseed(seed, minimum, maximum):
        random.seed(seed)
        return RandNums.randnums(minimum, maximum)

    @staticmethod
    def randnumfloat(minimum, maximum,):
        return random.uniform(minimum, maximum)

    @staticmethod
    def randumseedfloat(seed, minimum, maximum):
        random.seed(seed)
        return RandNums.randnumfloat(minimum, maximum)
