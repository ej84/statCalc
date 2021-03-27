from RandomGenerator.randnums import RandNums

class RandList:

    @staticmethod
    def randlist(length, seed, minimum, maximum):
        data = []
        while len(data) != length:
            data.append(RandNums.randumseed(seed, minimum, maximum))
        return data

    @staticmethod
    def randfloatlist(length, seed, minimum, maximum):
        data = []
        while len(data) != length:
            data.append(RandNums.randfloatseed(seed, minimum, maximum))
        return data
