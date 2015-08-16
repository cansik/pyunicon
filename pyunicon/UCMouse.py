from pyunicon.util.UCMouseKey import UCMouseKey
from util.UCFactory import UCFactory

__author__ = 'cansik'


class UCMouse(object):
    def __init__(self):
        self.__mouse = UCFactory.get_mouse()

    def move(self, x, y):
        self.__mouse.move(x, y)

    def move_relative(self, dx, dy):
        x, y = self.get_position()
        self.move(x.value + dx, y.value + dy)

    def get_position(self):
        return self.__mouse.get_position()

    def press(self, mouse_key):
        self.__mouse.press(mouse_key)

    def release(self, mouse_key):
        self.__mouse.release(mouse_key)

    def click(self, mouse_key):
        self.__mouse.press(mouse_key)
        self.__mouse.release(mouse_key)

    def click_left(self):
        self.click(UCMouseKey.UC_MOUSE_LEFT)

    def click_right(self):
        self.click(UCMouseKey.UC_MOUSE_RIGHT)