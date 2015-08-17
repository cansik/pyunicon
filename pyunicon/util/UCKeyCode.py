__author__ = 'cansik'


class UCKeyCode(object):
    def __init__(self, text, cocoa, x11, win32):
        self.Cocoa = cocoa
        self.X11 = text
        self.WinForm = win32