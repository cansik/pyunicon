from pyunicon.X11.X11Util import X11Util

__author__ = 'cansik'


class X11Screen(object):
    def __init__(self):
        self.__xlib = X11Util()

    def get_size(self):
        xwa = self.__xlib.get_xwindow_attributes()
        return xwa.width, xwa.height
