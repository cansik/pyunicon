from pyunicon.X11.X11Util import X11Util

__author__ = 'cansik'


class X11Keyboard(object):
    def __init__(self):
        self.__xlib = X11Util()

    def key_down(self, key_code):
        # todo: implement
        pass

    def key_up(self, key_code):
        # todo: implement
        pass

    def send_key(self, key_code):
        # self.__xlib.xsend_event(key_code, True)
        self.__xlib.send_key("x")
        pass