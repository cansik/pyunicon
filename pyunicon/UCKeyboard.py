from util.UCFactory import UCFactory

__author__ = 'cansik'


class UCKeyboard(object):
    def __init__(self):
        self.__keyboard = UCFactory.get_keyboard()

    def key_down(self, key_code):
        self.__keyboard.key_down(key_code)

    def key_up(self, key_code):
        self.__keyboard.key_up(key_code)

    def send_key(self, key_code):
        self.key_down(key_code)
        self.key_up(key_code)
