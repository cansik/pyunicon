from pyunicon.X11.X11Util import X11Util
from pyunicon.util import UCMouseKey

from Xlib import X
from Xlib.display import Display
from Xlib.ext.xtest import fake_input

__author__ = 'cansik'


class X11Mouse(object):
    def __init__(self):
        self.__xlib = X11Util()

    def move(self, x, y):
        self.__xlib.xwarp_pointer(x, y)

    def get_position(self):
        root_x, root_y, win_x, win_y = self.__xlib.xquery_pointer()
        return root_x.value, root_y.value

    def press(self, mouse_key):
        d = Display()
        fake_input(d, X.ButtonPress, self.__uckey_to_xkey(mouse_key))
        d.sync()

    def release(self, mouse_key):
        d = Display()
        fake_input(d, X.ButtonRelease, self.__uckey_to_xkey(mouse_key))
        d.sync()

    def __uckey_to_xkey(self, mouse_key):
        if mouse_key is UCMouseKey.UC_MOUSE_LEFT:
            return X.Button1
        elif mouse_key is UCMouseKey.UC_MOUSE_MIDDLE:
            return X.Button2
        elif mouse_key is UCMouseKey.UC_MOUSE_RIGHT:
            return X.Button3
