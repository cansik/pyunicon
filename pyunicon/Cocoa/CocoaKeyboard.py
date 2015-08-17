from Quartz.CoreGraphics import kCGHIDEventTap
from Quartz.CoreGraphics import CGEventPost
from Quartz.CoreGraphics import CGEventCreateKeyboardEvent
from objc._objc import NULL


class CocoaKeyboard(object):
    def __init__(self):
        pass

    def __sim_key(self, key_code, is_down):
        key = key_code.Cocoa

        if key is None:
            print("key not defined on cocoa!")
            pass

        key_event = CGEventCreateKeyboardEvent(NULL, key, is_down)
        CGEventPost(kCGHIDEventTap, key_event)

    def key_down(self, key_code):
        self.__sim_key(key_code, True)

    def key_up(self, key_code):
        self.__sim_key(key_code, False)
