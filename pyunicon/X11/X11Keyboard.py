from pyunicon.X11.X11Util import X11Util

from Xlib import X
from Xlib import XK
from Xlib.display import Display
from Xlib.ext.xtest import fake_input

__author__ = 'cansik'


class X11Keyboard(object):
    def __init__(self):
        self.__xlib = X11Util()

    def __send_key(self, x_event, key_code):
        key = key_code.X11

        if key is None:
            print("key not defined on X11!")
            pass

        d = Display()
        x11key = d.keysym_to_keycode(XK.string_to_keysym(key))
        fake_input(d, x_event, x11key)
        d.sync()

    def key_down(self, key_code):
        self.__send_key(X.KeyPress, key_code)

    def key_up(self, key_code):
        self.__send_key(X.KeyRelease, key_code)