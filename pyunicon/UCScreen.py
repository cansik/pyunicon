from util.UCFactory import UCFactory

__author__ = 'cansik'


class UCScreen(object):
    def __init__(self):
        self.__screen = UCFactory.get_screen()

    def get_size(self):
        return self.__screen.get_size()
