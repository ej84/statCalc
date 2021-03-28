import random


class ListGenerator:

    @staticmethod
    def listselect(data):
        return random.choice(data)

    @staticmethod
    def listseed(seed, data):
        random.seed(seed)
        return ListGenerator.listselect(data)

    @staticmethod
    def listselected(numbers, data):
        newlist = []
        while len(newlist) < numbers:
            newlist.append(ListGenerator.listselect(data))
        return newlist

    @staticmethod
    def listseeded(seed, numbers, data):
        random.seed(seed)
        return ListGenerator.listselected(numbers, data)
