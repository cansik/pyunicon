from pyunicon.X11.X11Util import X11Util
from pyunicon.util.UCMouseKey import UCMouseKey

__author__ = 'cansik'


class X11Mouse(object):
    def __init__(self):
        self.__xlib = X11Util()

    def move(self, x, y):
        self.__xlib.xwarp_pointer(x, y)

    def get_position(self):
        root_x, root_y, win_x, win_y = self.__xlib.xquery_pointer()
        return root_x.value, root_y.value

    def click(self, mouse_key):
        if mouse_key is UCMouseKey.UC_MOUSE_LEFT:
            pass
