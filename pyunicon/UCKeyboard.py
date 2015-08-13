from util.UCFactory import UCFactory

__author__ = 'cansik'


class UCScreen(object):
    def __init__(self):
        self.__keyboard = UCFactory.get_keyboard()

    def send_key(self, key_code):
        return self.__keyboard.send_key(key_code)