from util.UCFactory import UCFactory

__author__ = 'cansik'


class UCMouse(object):
    def __init__(self):
        self.__mouse = UCFactory.get_mouse()

    def move_mouse(self, x, y):
        self.__mouse.move_mouse(x, y)

    def move_mouse_relative(self, dx, dy):
        x, y = self.get_mouse_position()
        self.move_mouse(x.value + dx, y.value + dy)

    def get_mouse_position(self):
        return self.__mouse.get_mouse_position()
