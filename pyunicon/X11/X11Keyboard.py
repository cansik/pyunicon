from pyunicon.X11.X11Util import X11Util

__author__ = 'cansik'


class X11Keyboard(object):
    def __init__(self):
        self.__xlib = X11Util()

    def send_key(self, key_code):
        pass