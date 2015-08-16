from pyunicon.X11.X11Util import X11Util

from Xlib import X
from Xlib.display import Display
from Xlib.ext.xtest import fake_input

__author__ = 'cansik'


class X11Keyboard(object):
    def __init__(self):
        self.__xlib = X11Util()

    def key_down(self, key_code):
        d = Display()
        fake_input(d, X.KeyPress, key_code)
        d.sync()

    def key_up(self, key_code):
        d = Display()
        fake_input(d, X.KeyRelease, key_code)
        d.sync()