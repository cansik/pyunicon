from sys import platform as _platform
from pyunicon.Cocoa.CocoaKeyboard import CocoaKeyboard
from pyunicon.Cocoa.CocoaScreen import CocoaScreen
from pyunicon.X11.X11Keyboard import X11Keyboard

__author__ = 'cansik'


def get_os_peripherals():
    if _platform == "linux" or _platform == "linux2":
        from pyunicon.X11.X11Mouse import X11Mouse
        from pyunicon.X11.X11Screen import X11Screen
        return X11Mouse(), X11Keyboard(), X11Screen()

    elif _platform == "darwin":
        print('osx is not support atm!')
        from pyunicon.Cocoa.CocoaMouse import CocoaMouse
        return CocoaMouse(), CocoaKeyboard(), CocoaScreen()

    elif _platform == "win32":
        print('windows is not supported atm!')
        return None, None, None


class UCFactory(object):
    @staticmethod
    def get_mouse():
        return UCFactory.__mouse

    @staticmethod
    def get_keyboard():
        return UCFactory.__keyboard

    @staticmethod
    def get_screen():
        return UCFactory.__screen

    __mouse, __keyboard, __screen = get_os_peripherals()
