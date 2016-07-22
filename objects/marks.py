__author__ = 'pumarani'


class Marks(object):

    def __init__(self):
        self.plusOne = 0
        self.plusTwo = 0
        self.minusOne = 0
        self.minusTwo = 0
        self.zero = 0

    def get_marks(self):
        self.__dict__