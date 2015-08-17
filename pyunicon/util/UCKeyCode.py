__author__ = 'cansik'


class UCKeyCode(object):
    def __init__(self, cocoa_code, x11_code, win_code):
        self.Cocoa = cocoa_code
        self.X11 = x11_code
        self.WinForm = win_code